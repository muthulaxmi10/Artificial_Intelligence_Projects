# LangChain RAG Chatbot

## Project Overview

This project implements a **Retrieval-Augmented Generation (RAG) chatbot** using LangChain and FAISS.
The system retrieves relevant information from documents and generates answers using a Large Language Model (LLM).

The project demonstrates how vector databases and embeddings can be used to build intelligent question-answering systems.

---

## Features

* Document ingestion and preprocessing
* Embedding generation using OpenAI embeddings
* Vector storage using FAISS
* Semantic search for relevant document retrieval
* Question answering using a LangChain RAG pipeline

---

## Project Structure

```
langchain_rag_project
│
├── app/
│   ├── config.py
│   ├── embeddings.py
│   ├── rag_chain.py
│   └── vector_store.py
│
├── data/
│   └── docs.txt
│
├── app.py
├── ingest.py
├── requirements.txt
└── README.md
```

---

## Tech Stack

* Python
* LangChain
* OpenAI API
* FAISS Vector Database
* dotenv

---

## Installation

1. Clone the repository

```
git clone https://github.com/yourusername/langchain-rag-chatbot.git
```

2. Navigate to the project directory

```
cd langchain-rag-chatbot
```

3. Create virtual environment

```
python -m venv venv
```

4. Activate the virtual environment

Windows:

```
venv\Scripts\activate
```

5. Install dependencies

```
pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file in the project root and add your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

---

## Running the Project

1. Create the vector database

```
python ingest.py
```

2. Run the chatbot

```
python app.py
```

---

## Example Workflow

1. Documents are loaded from the `data` folder.
2. Text is converted into embeddings using OpenAI.
3. Embeddings are stored in a FAISS vector database.
4. When a user asks a question, the system retrieves the most relevant document chunks.
5. The retrieved context is passed to the language model to generate an answer.

---

## Future Improvements

* Add support for PDF document ingestion
* Build a web interface using Streamlit
* Implement conversational memory
* Deploy the application as a web service

---

## Note

The OpenAI API requires usage credits. If credits are unavailable, the application may not generate responses until credits are added.

---

## Author

Your Name
