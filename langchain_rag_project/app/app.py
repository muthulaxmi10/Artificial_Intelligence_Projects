# app/main.py
from app.rag_chain import get_rag_chain

rag_chain = get_rag_chain()

while True:
    query = input("\n Ask a question (or 'exit):")
    if query.lower() == "exit":
        break

    answer = rag_chain.invoke(query)
    print("\nAnswer")
    print(answer)