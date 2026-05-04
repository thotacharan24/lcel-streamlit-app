# 🚀 AI Translator (LangChain + Groq + FastAPI + Streamlit)

## 📌 Overview

This project is a simple **AI-powered translation system** that converts user input into another language (default: French).
It uses a **LangChain pipeline deployed via FastAPI (LangServe)** and a **Streamlit frontend UI**.

The system demonstrates:

* LLM integration using Groq (LLaMA 3)
* LangChain runnable pipelines
* FastAPI deployment with LangServe
* Interactive frontend using Streamlit

---

## 🏗️ Architecture

Frontend (Streamlit)
⬇
FastAPI Server (LangServe)
⬇
LangChain Pipeline
⬇
Groq LLM (LLaMA 3.3)

---

## ⚙️ Tech Stack

* **Backend:** FastAPI, LangServe
* **Frontend:** Streamlit
* **LLM:** Groq (LLaMA 3.3-70B)
* **Framework:** LangChain
* **Other Tools:** Python, dotenv

---

## 📂 Project Structure

```
project/
│
├── api/
│   └── main.py          # FastAPI + LangServe app
│
├── frontend/
│   └── app.py           # Streamlit UI
│
├── .env                 # API keys
├── requirements.txt
└── README.md
```

---

## 🔑 Setup Instructions

### 1. Clone the Repository

```
git clone <your-repo-url>
cd <project-folder>
```

---

### 2. Create Virtual Environment

```
python -m venv venv
```

Activate:

* Windows:

```
venv\Scripts\activate
```

* Mac/Linux:

```
source venv/bin/activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Add Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Running the Application

### Start FastAPI Server

```
python api/main.py
```

OR

```
uvicorn api.main:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

---

### Start Streamlit App

```
streamlit run frontend/app.py
```

---

## 🧠 How It Works

### 1. Prompt Design

The system uses a structured prompt:

```
System: Translate the following into {language}
User: {text}
```

---

### 2. LangChain Pipeline

```
Prompt → Groq Model → Output Parser
```

* `ChatPromptTemplate` → formats input
* `ChatGroq` → generates response
* `StrOutputParser` → extracts clean output

---

### 3. API Endpoint

LangServe exposes:

```
POST /chain/invoke
```

Request:

```
{
  "input": {
    "topic": "Hello"
  }
}
```

---

### 4. Frontend Flow

* User enters text
* Streamlit sends request → FastAPI
* API calls LangChain pipeline
* Response displayed in UI

---

## 📦 Requirements

```
langchain
python-dotenv
ipykernel
langchain-community
pypdf
bs4
arxiv
pymupdf
wikipedia
langchain-text-splitters
langchain-openai
chromadb
sentence_transformers
langchain_huggingface
faiss-cpu
langchain_chroma
duckdb
pandas
openai
langchain-groq
duckduckgo_search==5.3.1b1
mysql-connector-python
SQLAlchemy
validators==0.28.1
youtube_transcript_api
unstructured
pytube
numexpr
huggingface_hub
```

---

## 🚨 Known Issues

* Input variable mismatch:

  * API expects `{text}` and `{language}`
  * Frontend sends `{topic}`
    👉 Needs alignment

* No error handling for invalid responses

* No logging or monitoring

---

## 🔥 Future Improvements

* Add multi-language selection
* Add streaming responses
* Add error handling & retries
* Integrate logging (LangSmith)
* Dockerize application
* Deploy on cloud (AWS / GCP)

---

## 💡 Key Learnings

* How LangChain pipelines work
* How to expose chains via APIs
* How to connect frontend with LLM backend
* Importance of prompt structure
* Basics of production-ready AI systems

---

## 📜 License

This project is for learning and demonstration purposes.

---

## ✨ Author

Your Name
