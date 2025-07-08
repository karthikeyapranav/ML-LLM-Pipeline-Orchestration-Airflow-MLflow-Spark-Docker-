from fastapi import FastAPI

app = FastAPI()

from .model_handler import predict_quality
from .model_wrapper import load_model

model = load_model()

@app.get("/")
def root():
    return {"message": "Wine Quality Prediction API"}

@app.post("/predict/")
def predict(features: dict):
    return predict_quality(model, features)
