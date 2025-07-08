#  End-to-End ML + LLM Pipeline Orchestration

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Built with Docker](https://img.shields.io/badge/Built%20with-Docker-blue.svg)](https://www.docker.com/)
[![Built with Airflow](https://img.shields.io/badge/Orchestration-Apache%20Airflow-orange.svg)](https://airflow.apache.org/)
[![MLflow Tracking](https://img.shields.io/badge/ML%20Tracking-MLflow-green.svg)](https://mlflow.org/)
[![FastAPI](https://img.shields.io/badge/Web%20Services-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)

This project presents a robust, full-cycle orchestration pipeline designed for both traditional Machine Learning (ML) models and modern Retrieval-Augmented Generation (RAG) style Large Language Model (LLM) systems. It demonstrates automated data processing, model training, versioning, and scalable deployment by leveraging a powerful suite of open-source MLOps tools.

---

##  Features at a Glance

* **Complete MLOps Cycle:** From raw data to deployed model, experience an end-to-end automated workflow.
* **Hybrid AI Approach:** Seamlessly integrates a classical ML model with a cutting-edge RAG-style LLM.
* **Scalable & Efficient:** Utilizes Apache Spark for distributed data processing.
* **Reproducible ML:** MLflow ensures comprehensive tracking, versioning, and registration of ML models.
* **Production-Ready Deployment:** FastAPI powers the web services for real-time inference.
* **Containerized Environments:** Docker and Docker Compose provide consistent and isolated setups.
* **Smart LLM Interactions:** RAG system for contextualized question answering from custom documents.

---

##  Core Technologies

| Category      | Technology            | Description                                            |
| :------------ | :-------------------- | :----------------------------------------------------- |
| **Orchestration** | Apache Airflow        | Workflow management for scheduling and monitoring DAGs. |
| **Data Processing** | Apache Spark (PySpark) | Distributed processing engine for big data.            |
| **MLOps** | MLflow                | Model tracking, registry, and deployment.               |
| **Web Services** | FastAPI               | High-performance, easy-to-use web framework.          |
| **Vector DB** | FAISS                 | Efficient similarity search for dense vectors.         |
| **LLMs & Embeddings** | Hugging Face transformers & sentence-transformers | Pre-trained models for language tasks and embeddings. |
| **Containerization** | Docker & Docker Compose | Packaging and orchestrating applications in isolated containers. |

---

##  Project Structure

ML_LLM_PIPELINE/
├── airflow/                 # Airflow DAGs for ML pipeline orchestration
├── api/                     # FastAPI app for ML model inference
├── data/                    # Shared directory for ML input data (e.g., WineQuality.csv)
├── models/                  # Stores trained ML models (e.g., model.pkl)
├── mlruns/                  # MLflow tracking server data
├── rag/                     # Part B: RAG-style LLM Pipeline components
│   ├── ingest.py            # Script for document ingestion, chunking, embedding, and FAISS index creation
│   ├── query.py             # Core RAG logic: retrieve relevant chunks, generate answer with LLM
│   ├── app.py               # FastAPI server for the RAG endpoint
│   ├── vectorstore/         # Stores FAISS index and embeddings
│   ├── data/                # Stores raw input documents for RAG (e.g., PDFs, CSVs)
│   ├── Dockerfile           # Dockerfile for building the RAG application image
│   ├── requirements.txt     # Python dependencies for the RAG application
│   └── docker-compose.yml   # Docker Compose for orchestrating the RAG service
├── scripts/                 # PySpark training script for ML pipeline
├── docker-compose.yml       # Main Docker Compose for the entire ML pipeline (Part A)
└── README.md                # This file (You are here!)

---

##  Part A: Wine Quality Prediction (ML Pipeline)

This section automates an end-to-end machine learning workflow for predicting wine quality.

###  Key Features:

* **Automated Training DAG:** An Apache Airflow DAG orchestrates the entire ML training process, from data preparation to model registration.
* **Scalable Data Transformation:** Leverages PySpark for efficient and scalable data preprocessing and feature engineering.
* **MLflow Integration:** Models are meticulously tracked, versioned, and registered into the MLflow Model Registry, ensuring reproducibility and streamlined deployment of "production" models.
* **Production Model Serving:** The latest production-ready model from MLflow is automatically loaded and served via a dedicated FastAPI endpoint for real-time inference.
* **Containerized Environment:** The entire ML pipeline (Airflow, Spark, MLflow, FastAPI) runs seamlessly within Docker containers, guaranteeing consistent environments across development and production.

### ⚙️ How to Run Part A:

1.  **Ensure Docker Desktop is running.**
2.  **Navigate to the root directory** of the project: `ML_LLM_Pipeline/`.
3.  **Start all services** defined in the main `docker-compose.yml` (this will bring up Airflow, MLflow, Spark, and the ML API):
    ```bash
    docker-compose up --build
    ```
4.  **Access Airflow UI:** Once services are up, navigate to [http://localhost:8080](http://localhost:8080) in your browser.
5.  **Unpause and Trigger DAG:** Find the ML pipeline DAG (e.g., `wine_quality_prediction_dag`) in the Airflow UI, unpause it, and manually trigger it. This will initiate the data processing, training, and model registration steps.
6.  **Access MLflow UI (Optional):** Monitor experiments and registered models at [http://localhost:5000](http://localhost:5000).
7.  **Access ML Prediction API:** The FastAPI documentation for the ML model's prediction endpoint will be available at [http://localhost:8000/docs](http://localhost:8000/docs).

---

##  Part B: RAG-style LLM Pipeline (Mini POC)

This section implements a Retrieval-Augmented Generation (RAG) system, enabling a small open-source LLM to answer questions based on custom, ingested documents.

###  Key Features:

* **Document Ingestion:** Supports loading and processing various document types (e.g., PDF, CSV).
* **Semantic Search:** Utilizes `sentence-transformers` for creating robust embeddings and FAISS as a high-performance vector database for efficient semantic retrieval of relevant document chunks.
* **Contextualized Generation:** A compact, open-source LLM (e.g., `google/flan-t5-small`) is augmented with retrieved context, enabling it to provide accurate and relevant answers to natural language queries.
* **FastAPI Q&A Interface:** A dedicated FastAPI endpoint (`/rag-query/`) provides a clean REST interface for interacting with the RAG system.
* **Self-Contained Deployment:** The entire RAG component is independently containerized using its own `Dockerfile` and `docker-compose.yml` within the `rag/` directory, ensuring modularity and easy integration.

### ⚙ How to Run Part B:

1.  **Navigate to the RAG directory:**
    ```bash
    cd ML_LLM_Pipeline/rag
    ```
2.  **Place your data:**
    Ensure your PDF documents (e.g., `Global warming.pdf`) are located in `ML_LLM_Pipeline/rag/data/`.
3.  **Run Ingestion (First time & whenever data changes):**
    This crucial step processes your documents, creates embeddings, and builds the FAISS index on your host machine. These artifacts will then be mounted into the Docker container.
    ```bash
    python ingest.py
    ```
    You should see confirmation like: ` Indexed X chunks from: rag/data/Global warming.pdf.`
4.  **Build the Docker Image:**
    ```bash
    docker-compose build rag-app
    ```
    This command reads the `Dockerfile` and `requirements.txt` to create the container image for your RAG service. **Note:** This may take some time as it downloads base images and installs libraries, including the LLM model weights.
5.  **Start the RAG Service:**
    ```bash
    docker-compose up rag-app
    ```
    This will start the FastAPI application inside a Docker container. The application will be accessible via [http://localhost:8002](http://localhost:8002). You will see output from Uvicorn in your terminal. This command will keep running and attach to the container's logs.
6.  **Test the RAG API:**
    Open your web browser or use `curl` from a new terminal window (while the `docker-compose up rag-app` command is still running):
    * **Health Check:**
        ```
        http://localhost:8002/
        ```
        Expected output: `{"message": "API running"}`
    * **Query RAG System:**
        ```
        http://localhost:8002/rag-query/?question=What is global warming?
        ```
        (Replace "What is global warming?" with a relevant question from your PDF content.)
        You should receive a JSON response containing the original question, the retrieved context, and the LLM's generated answer.
7.  **Stop the RAG Service:**
    To stop the RAG service, go back to the terminal where `docker-compose up rag-app` is running and press `Ctrl+C`.

---

##  Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please open an issue or submit a pull request.

---

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

##  Acknowledgments

* The open-source community for providing these amazing tools.
* Your inspiration for making this README more beautiful!
