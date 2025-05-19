# curl https://api.openai.com/v1/models \
#   -H "Authorization: Bearer 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" \
#   -H "OpenAI-Organization: org-9E7FNdltkUqAXx96YDCY8ZG8" \
#   -H "OpenAI-Project: $PROJECT_ID"

curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer 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" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-3.5-turbo
    "messages": [{"role": "user", "content": "Tell me a three sentence bedtime story about a unicorn."}]
  }'