# app/vector store.py
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.embeddings import get_embeddings
from app.config import DB_PATH


def create_vector_store(text: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.create_documents([text])
    embeddings = get_embeddings()

    db = FAISS.from_documents(docs, embeddings)
    db.save_local(DB_PATH)
    

    return db
 
def load_vector_store():
    embeddings = get_embeddings()
    return FAISS.load_local(
        DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )