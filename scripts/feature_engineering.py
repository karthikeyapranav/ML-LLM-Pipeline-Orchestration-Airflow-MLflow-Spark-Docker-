# scripts/feature_engineering.py
import pandas as pd
import os

def feature_engineering():
    os.makedirs("data/processed", exist_ok=True)

    # Read from parquet
    df = pd.read_parquet("data/processed/wine_data.parquet")

    # Basic Cleaning
    df.dropna(inplace=True)

    # Map quality scores into binary classification: 0 = bad (<=5), 1 = good (>=6)
    df['label'] = df['quality'].apply(lambda q: 1 if q >= 6 else 0)

    # Drop original quality column
    df.drop(columns=['quality'], inplace=True)

    # Save final processed features
    df.to_csv("data/processed/wine_features.csv", index=False)
    print("✅ Feature engineering complete. Saved to data/processed/wine_features.csv")

if __name__ == "__main__":
    feature_engineering()
