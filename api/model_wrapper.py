import joblib
import numpy as np

model = joblib.load("models/best_model.pkl")

def predict_quality(data: list):
    return int(model.predict([data])[0])

def load_model():
    model_path = "models/best_model.pkl"
    return joblib.load(model_path)