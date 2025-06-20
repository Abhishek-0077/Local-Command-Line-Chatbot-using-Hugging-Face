# Local-Command-Line-Chatbot-using-Hugging-Face


This is a lightweight chatbot that:

- Runs fully on CPU
- Uses Hugging Face Transformers pipeline
- Loads `microsoft/phi-2` model for text generation
- CLI-based interface for easy interaction

---

## 🗂 Project Structure

| File | Description |
|---|---|
| `model_loader.py` | Loads the Phi-2 model |
| `chat_memory.py` | Maintains recent chat history |
| `interface.py` | CLI interface |

---

## 🔧 Setup Instructions
Create a virtual environment

-python -m venv venv
-source venv/bin/activate 
-pip install transformers torch

python interface.py

## 🎯 Example Usage

You: Hello!
Assistant: Hi! How can I help you?

You: What is the capital of India?
Assistant: The answer is New Delhi.

You: Who is the prime minister of India?
Assistant: The answer is Narendra Modi.

