# scripts/data_ingestion.py
from pyspark.sql import SparkSession
import os

def ingest_data():
    # Make directory if it doesn't exist
    os.makedirs("data/processed", exist_ok=True)

    spark = SparkSession.builder.appName("WineIngestion").getOrCreate()
    df = spark.read.csv("data/winequality-red.csv", header=True, inferSchema=True)
    df.write.parquet("data/processed/wine_data.parquet", mode="overwrite")
    spark.stop()

if __name__ == "__main__":
    ingest_data()
