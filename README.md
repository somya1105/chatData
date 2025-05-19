# 📚 Chat with Data

A Streamlit-based application that enables users to **chat with their PDFs** using **LangChain**, **FAISS**, and **OpenAI/HuggingFace models**.

---

## 🚀 Quickstart

### 1. Set up the virtual environment

```bash
pip install virtualenv
virtualenv venv --system-site-packages
source venv/bin/activate
```

> ✅ Ensure your Python version is **3.10**

---

### 2. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

If `requirements.txt` is not yet created, use:

```bash
pip install streamlit pypdf2 langchain python-dotenv faiss-cpu openai huggingface_hub
```

---

### 3. Run the app

```bash
streamlit run app.py
```

---

## 🧠 What This App Does

- Accepts **multiple PDF documents**
- Extracts and chunks the text
- Generates embeddings via **HuggingFace Instruct models**
- Stores vectors locally in **FAISS**
- Enables conversational querying over documents using **LangChain's ConversationalRetrievalChain**
- Supports chat history (memory buffer)

---

## 🧩 Product at a go

### What kind of questions can users ask?
- Both **factual** (e.g., "What does this page say?") and **analytical** (e.g., "What are the common concerns?")

### What documents are supported in v1?
- Currently supports **PDFs**
- Future support: transcripts, notes, video summaries (text)

### Stateless or Chat History?
- **Chat history is enabled** in v1 using `ConversationBufferMemory`

### Should responses include source citation?
- **Not implemented yet**, but can be added using metadata from the retriever
- Can be part of v1
---

## 🎨 Frontend

- Minimal, **Slack-style chat UI** in Streamlit
- Custom HTML templates for bot and user messages
- Sidebar for PDFs uploaded & processing button
- Input box disabled until PDFs are processed

---

## 🔐 Authentication & Security

- **No real authentication in v1** – mocked for now
- Future plans:
  - OAuth or API key integration
  - Project-specific data access control

---

## ⚙️ Architecture Overview

- **Frontend**: Streamlit
- **Backend**:
  - PDF parsing: `PyPDF2`
  - Embeddings: `HuggingFaceInstructEmbeddings`
  - Vector DB: `FAISS` (local)
  - Language model: `OpenAI GPT-3.5`
- **Memory**: `ConversationBufferMemory` (LangChain)

---

## 🔮 Roadmap for v1

| Feature                           | Status | Notes                                      |
|-----------------------------------|--------|--------------------------------------------|
| Multi-user chat                   | ❌     | Potential for v2/v3 for collaboration      |
| Source citations                  | ⚠️     | Can be added via retriever metadata        |
| Selective file querying           | ❌     | Useful for large projects                  |
| Rate limiting / API usage control | ⚠️     | Important as usage scales                  |
| Query logging for fine-tuning     | ❌     | Should be added for future improvements    |
| External knowledge base support   | ❌     | Could expand scope beyond just PDF data    |
| Multiple file type support        | ❌     | Can be completed in v1 if needed           |

---

## 📁 Sample `.env`

Create a `.env` file at root:

```env
OPENAI_API_KEY=sk-...
```

> Or set directly in `app.py` if testing (not recommended for production)

---

## 📌 Developer Commands

Clean & re-init environment:

```bash
rm -rf venv && python3 -m venv venv && source venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
```

---
