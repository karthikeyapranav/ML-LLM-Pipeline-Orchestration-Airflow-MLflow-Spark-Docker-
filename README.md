🚀 End-to-End ML + LLM Pipeline Orchestration
This project showcases a robust, full-cycle orchestration pipeline for both a traditional Machine Learning (ML) model and a modern Retrieval-Augmented Generation (RAG) style Large Language Model (LLM) system. Leveraging a powerful suite of open-source MLOps tools, this pipeline demonstrates automated data processing, model training, versioning, and scalable deployment.

🛠️ Core Technologies
This comprehensive pipeline is built upon the following key technologies:

Orchestration: Apache Airflow

Data Processing: Apache Spark (PySpark)

ML Model Tracking & Registry: MLflow

Web Services: FastAPI

Vector Database: FAISS

LLMs & Embeddings: Hugging Face transformers & sentence-transformers

Containerization: Docker & Docker Compose

📂 Project Structure
ML_LLM_PIPELINE/
├── airflow/             # Airflow DAGs for ML pipeline orchestration
├── api/                 # FastAPI app for ML model inference
├── data/                # Shared directory for ML input data (e.g., WineQuality.csv)
├── models/              # Stores trained ML models (e.g., model.pkl)
├── mlruns/              # MLflow tracking server data
├── rag/                 # **Part B: RAG-style LLM Pipeline components**
│   ├── ingest.py        # Script for document ingestion, chunking, embedding, and FAISS index creation
│   ├── query.py         # Core RAG logic: retrieve relevant chunks, generate answer with LLM
│   ├── app.py           # FastAPI server for the RAG endpoint
│   ├── vectorstore/     # Stores FAISS index and embeddings
│   ├── data/            # Stores raw input documents for RAG (e.g., PDFs, CSVs)
│   ├── Dockerfile       # Dockerfile for building the RAG application image
│   ├── requirements.txt # Python dependencies for the RAG application
│   └── docker-compose.yml # Docker Compose for orchestrating the RAG service
├── scripts/             # PySpark training script for ML pipeline
├── docker-compose.yml   # Main Docker Compose for the entire ML pipeline (Part A)
└── README.md            # This file

🍷 Part A: Wine Quality Prediction (ML Pipeline)
This section focuses on the end-to-end automation of a machine learning workflow for predicting wine quality.

✨ Features:
Automated Training DAG: An Airflow DAG orchestrates the entire ML training process, from data preparation to model registration.

Scalable Data Transformation: PySpark is utilized for efficient and scalable data preprocessing and feature engineering.

MLflow Integration: Models are tracked, versioned, and registered into the MLflow Model Registry, promoting reproducibility and easy deployment of "production" models.

Production Model Serving: The latest production-ready model from MLflow is automatically loaded and served via a dedicated FastAPI endpoint for real-time inference.

Containerized Environment: The entire ML pipeline (Airflow, Spark, MLflow, FastAPI) runs seamlessly within Docker containers, ensuring consistent environments.

⚙️ How to Run Part A:
Ensure Docker Desktop is running.

Navigate to the root directory of the project: ML_LLM_Pipeline/.

Start all services defined in the main docker-compose.yml (this will bring up Airflow, MLflow, Spark, and the ML API):

docker-compose up --build

Access Airflow UI: Once services are up, navigate to http://localhost:8080 in your browser.

Unpause and Trigger DAG: Find the ML pipeline DAG (e.g., wine_quality_prediction_dag) in the Airflow UI, unpause it, and manually trigger it. This will initiate the data processing, training, and model registration steps.

Access MLflow UI (Optional): Monitor experiments and registered models at http://localhost:5000.

Access ML Prediction API: The FastAPI documentation for the ML model's prediction endpoint will be available at http://localhost:8000/docs.

🧠 Part B: RAG-style LLM Pipeline (Mini POC)
This section implements a Retrieval-Augmented Generation (RAG) system, enabling a small open-source LLM to answer questions based on custom, ingested documents.

✨ Features:
Document Ingestion: Supports loading and processing PDF/CSV documents.

Semantic Search: Utilizes sentence-transformers for creating embeddings and FAISS as a high-performance vector database for efficient semantic retrieval of relevant document chunks.

Contextualized Generation: A small, open-source LLM (google/flan-t5-small) is augmented with retrieved context to provide accurate and relevant answers to natural language queries.

FastAPI Q&A Interface: A dedicated FastAPI endpoint (/rag-query/) provides a clean REST interface for interacting with the RAG system.

Self-Contained Deployment: The entire RAG component is independently containerized using its own Dockerfile and docker-compose.yml within the rag/ directory, ensuring modularity.

⚙️ How to Run Part B:
Navigate to the RAG directory:

cd ML_LLM_Pipeline/rag

Place your data:
Ensure your PDF documents (e.g., Global warming.pdf) are located in ML_LLM_Pipeline/rag/data/.

Run Ingestion (First time & whenever data changes):
This step processes your documents, creates embeddings, and builds the FAISS index on your host machine. These artifacts will be mounted into the Docker container.

python ingest.py

You should see confirmation like ✅ Indexed X chunks from: rag/data/Global warming.pdf.

Build the Docker Image:

docker-compose build rag-app

This command reads the Dockerfile and requirements.txt to create the container image for your RAG service. This may take some time as it downloads base images and installs libraries, including the LLM model weights.

Start the RAG Service:

docker-compose up rag-app

This will start the FastAPI application inside a Docker container. The application will be accessible via http://localhost:8002. You will see output from Uvicorn in your terminal. This command will keep running and attach to the container's logs.

Test the RAG API:
Open your web browser or use curl from a new terminal window (while the docker-compose up command is still running):

Health Check:

http://localhost:8002/

Expected output: {"message": "API running"}

Query RAG System:

http://localhost:8002/rag-query/?question=What is global warming?

(Replace "What is global warming?" with a relevant question from your PDF content.)
You should receive a JSON response containing the original question, the retrieved context, and the LLM's generated answer.

Stop the RAG Service:
To stop the RAG service, go back to the terminal where docker-compose up rag-app is running and press Ctrl+C.

