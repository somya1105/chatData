import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI
from htmlTemplates import css, bot_template, user_template


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        reader = PdfReader(pdf)
        for page in reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    # embeddings = OpenAIEmbeddings()
    embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

def handle_user_question(user_question):
    if not st.session_state.conversation_chains:
        st.error("❗ Please upload and process PDFs first.")
        return

    response = st.session_state.conversation_chains({"question": user_question})
    st.session_state.chat_history = response.get("chat_history")
    for i, message in enumerate(reversed(st.session_state.chat_history)):
        if i % 2 == 0:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)


def main():
    load_dotenv()
    import os
    os.environ["OPENAI_API_KEY"] = "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"
    st.set_page_config(page_title="Chat with your PDFs", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation_chains" not in st.session_state:
        st.session_state.conversation_chains = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None 

    st.header("Chat with your PDFs :books:")
    # Disable the text input until PDFs are processed
    user_question = st.text_input("Ask a question about your documents:")
    if st.session_state.conversation_chains is None:
        st.warning("👆 Please upload your PDFs in the sidebar and click 'Process' first.")
    if user_question:
        handle_user_question(user_question)
    
    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your PDF files here and click on 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                #get pdf text
                if pdf_docs:
                    raw_text = get_pdf_text(pdf_docs)
                    #get the text chunks
                    text_chunks = get_text_chunks(raw_text)
                    #create vector store
                    vectorstore = get_vectorstore(text_chunks)

                #create conversation chain
                st.session_state.conversation_chains = get_conversation_chain(vectorstore)
                print(st.session_state.conversation_chains)

    #user input

if __name__ == "__main__":
    main()
