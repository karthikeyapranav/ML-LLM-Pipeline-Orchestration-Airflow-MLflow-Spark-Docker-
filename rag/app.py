from fastapi import FastAPI, Query
from query import RAGQueryEngine

app = FastAPI()
engine = RAGQueryEngine()

@app.get("/")
def home():
    return {"message": "API running"}

@app.get("/rag-query/")
def query_rag(question: str = Query(..., description="Your question to the LLM")):
    response = engine.query(question)
    return response
