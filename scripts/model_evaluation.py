# scripts/model_evaluation.py
import pandas as pd
import mlflow
from sklearn.metrics import accuracy_score
import joblib

def evaluate():
    model = mlflow.sklearn.load_model("runs:/{run_id}/wine_model")  # Replace with your run_id
    X_test = pd.read_csv("data/processed/X_test.csv")
    y_test = pd.read_csv("data/processed/y_test.csv")

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    mlflow.log_metric("accuracy", acc)
    joblib.dump(model, "models/final_model.pkl")

if __name__ == "__main__":
    evaluate()
