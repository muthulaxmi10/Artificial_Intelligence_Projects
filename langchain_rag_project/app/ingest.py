# ingest.py
from app.vector_store import create_vector_store

with open("data/docs.txt", "r", encoding="utf-8") as f:
    text = f.read()

create_vector_store(text)
print("vector store created")