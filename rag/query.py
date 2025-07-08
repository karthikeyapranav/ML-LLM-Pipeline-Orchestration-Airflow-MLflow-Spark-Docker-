import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import pipeline

class RAGQueryEngine:
    def __init__(self):
        self.emb_model = SentenceTransformer("all-MiniLM-L6-v2")
        self.generator = pipeline("text2text-generation", model="google/flan-t5-small")
        self.index = faiss.read_index("rag/vectorstore/index.faiss")
        self.chunks = np.load("rag/vectorstore/chunks.npy", allow_pickle=True)

    def query(self, question, top_k=3):
        q_embed = self.emb_model.encode([question])
        _, I = self.index.search(np.array(q_embed), top_k)
        context = "\n".join([self.chunks[i] for i in I[0]])

        prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
        response = self.generator(prompt, max_length=128, do_sample=False)

        return {
            "question": question,
            "retrieved_context": context,
            "generated_answer": response[0]["generated_text"]
        }
