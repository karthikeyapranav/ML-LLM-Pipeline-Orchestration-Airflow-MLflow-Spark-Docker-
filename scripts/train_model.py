# scripts/train_model.py

import pandas as pd
import os
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from mlflow.tracking import MlflowClient

def train():
    df = pd.read_csv("data/processed/wine_features.csv")
    X = df.drop("label", axis=1)
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    with mlflow.start_run() as run:
        clf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
        clf.fit(X_train, y_train)

        y_pred = clf.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)

        mlflow.log_param("n_estimators", 100)
        mlflow.log_param("max_depth", 5)
        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("f1_score", f1)

        # Log model
        mlflow.sklearn.log_model(clf, "model")

        # Register model
        model_name = "wine_quality_model"
        result = mlflow.register_model(
            model_uri=f"runs:/{run.info.run_id}/model",
            name=model_name
        )

        print(f"✅ Model trained and logged. Accuracy: {acc:.4f}, F1: {f1:.4f}")

        # Update alias to "production"
        client = MlflowClient()
        client.set_registered_model_alias(model_name, "production", result.version)
        print(f"🚀 Model version {result.version} registered and aliased as 'production'.")

if __name__ == "__main__":
    os.environ["MLFLOW_TRACKING_URI"] = "http://127.0.0.1:5000"
    #mlflow.set_tracking_uri("http://127.0.0.1:5000")
    mlflow.set_tracking_uri("file:///D:/ML_LLM_Pipeline/mlruns")
    mlflow.set_experiment("wine-quality-exp")
    train()
