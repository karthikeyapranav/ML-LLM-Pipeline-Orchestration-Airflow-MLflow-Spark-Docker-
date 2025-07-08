from sentence_transformers import SentenceTransformer
from PyPDF2 import PdfReader
import faiss
import numpy as np
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

def read_pdf(path):
    reader = PdfReader(path)
    text = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return text

def chunk_text(text, chunk_size=200):
    words = text.split()
    return [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

def create_faiss_index(chunks, embedding_model):
    embeddings = embedding_model.encode(chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return index, embeddings, chunks

if __name__ == "__main__":
    pdf_path = "D:/ML_LLM_Pipeline/rag/data/global_warming.pdf"
    text = read_pdf(pdf_path)
    chunks = chunk_text(text, chunk_size=150)  # smaller chunks for better generation
    index, embeddings, chunk_list = create_faiss_index(chunks, model)

    os.makedirs("rag/vectorstore", exist_ok=True)
    faiss.write_index(index, "rag/vectorstore/index.faiss")
    np.save("rag/vectorstore/chunks.npy", np.array(chunk_list))
    print(f"✅ Indexed {len(chunks)} chunks from: {pdf_path}")
