from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
import os

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

class Memory:
    def __init__(self, index_path="memory_index"):
        self.index_path = index_path
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        if os.path.exists(index_path):
            self.db = FAISS.load_local(index_path, self.embeddings, allow_dangerous_deserialization=True)
        else:
            self.db = FAISS.from_texts(["Initial memory"], self.embeddings)
            self.db.save_local(index_path)

    def store(self, text):
        self.db.add_texts([text])
        self.db.save_local(self.index_path)

    def recall(self, query, k=3):
        results = self.db.similarity_search(query, k=k)
        return [r.page_content for r in results]
