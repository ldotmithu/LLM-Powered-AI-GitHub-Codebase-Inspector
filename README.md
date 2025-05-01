# 🧠 LLM-Powered GitHub Codebase Inspector

Welcome to the **LLM GitHub Codebase Inspector** — an AI-powered Streamlit app that helps you **analyze, summarize, and query any GitHub repository** using advanced Large Language Models (LLMs) and vector-based retrieval. 🚀

---

## 🔍 Features

- 🧠 **Smart Summarization**  
  Generate a clear and concise summary of any GitHub project using an LLM.

- 💬 **Ask Code Questions**  
  Ask natural language questions about the repo’s functionality, logic, or structure.

- 🧱 **Chunking & Embedding**  
  Splits the codebase into chunks and creates embeddings for semantic search.

- 📦 **Vector Store Integration**  
  Uses vector databases to retrieve the most relevant code blocks for your queries.

---



## 🚀 How It Works

1. **Paste** a GitHub repository URL.
2. The app **clones** the repo and filters for key file types (`.py`, `.js`, `.md`, etc.).
3. Code is **chunked**, **embedded**, and stored in a vector store.
4. The LLM provides:
   - 📄 A **project summary**
   - 💡 Contextual **answers to your questions**

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **LLM**: Google and mistral 
- **Embeddings**: Hugging Face sentence transformers
- **Vector Store**: FAISS
- **Git Integration**: LangChain GitLoader

---

## 📦 Installation

```bash
git clone https://github.com/ldotmithu/LLM-Powered-AI-GitHub-Codebase-Inspector.git
cd LLM-Powered-AI-GitHub-Codebase-Inspector
pip install -r requirements.txt
streamlit run main.py

```
## 🧪 Use Case Scenarios

- 📘 Exploring unfamiliar open-source repositories

- 🧑‍💻 Onboarding new developers to a codebase

- 🎓 Learning codebases by asking natural language questions

- 🔎 Conducting audits and documentation generation

## 🙌 Credits

- Built with ❤️ by Mithurshan

---

## 📸  Glance of a project:- 

![image](https://github.com/ldotmithu/Dataset/blob/main/Screenshot%202025-05-01%20165940.png)

---
