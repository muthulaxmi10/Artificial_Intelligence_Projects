# app/congig.py
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DATA_PATH = "data/"
DB_PATH = "vectorstore/faiss_index/"