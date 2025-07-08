# scripts/model_training.py
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train():
    X = pd.read_csv("data/processed/X.csv")
    y = pd.read_csv("data/processed/y.csv")
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    with mlflow.start_run():
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train.values.ravel())

        mlflow.sklearn.log_model(model, "wine_model")
        mlflow.log_params(model.get_params())

        # Save test set for evaluation
        X_test.to_csv("data/processed/X_test.csv", index=False)
        y_test.to_csv("data/processed/y_test.csv", index=False)

if __name__ == "__main__":
    train()
