#  Project Summary: Comprehensive ML + LLM Pipeline

This project delivers an end-to-end automated pipeline for both traditional Machine Learning (ML) and modern Retrieval-Augmented Generation (RAG) Large Language Model (LLM) systems. It serves as a practical demonstration of MLOps best practices, leveraging a robust suite of open-source tools for orchestration, data processing, model management, and deployment.

---

##  Key Components & Their Roles

| Component           | Purpose                                                              |
| :------------------ | :------------------------------------------------------------------- |
| **Apache Airflow** | Orchestrates and automates the ML training and deployment pipeline.  |
| **Apache PySpark** | Enables scalable data transformation and processing for ML.          |
| **MLflow** | Provides robust model tracking, versioning, and a model registry.    |
| **FastAPI** | Serves high-performance REST APIs for both ML predictions and RAG Q&A. |
| **FAISS** | Acts as an efficient vector database for semantic search in RAG.     |
| **LLMs & Embeddings** | Powers the RAG system with contextualized text generation.             |
| **Docker** | Ensures consistent, isolated, and portable environments for all services. |

---

## Project Highlights

### Part A: ML Pipeline (Wine Quality Prediction) 

* **Automated ML Lifecycle:** A complete ML pipeline, from raw data to a production-ready API, is fully automated via Airflow DAGs.
* **Scalable Data Handling:** Leverages PySpark for efficient and distributed data preprocessing, suitable for large datasets.
* **Reproducible ML:** MLflow ensures all experiments, models, and artifacts are meticulously tracked, enabling easy reproducibility and version control.
* **Production-Ready Deployment:** The latest production model is automatically deployed and served through a FastAPI microservice, ready for seamless integration.

### Part B: RAG-style LLM Pipeline 

* **Context-Aware AI:** Successfully implemented a RAG system that augments a small LLM (`google/flan-t5-small`) with retrieved information from custom documents, enabling more accurate and grounded answers.
* **Efficient Information Retrieval:** Utilizes `sentence-transformers` for high-quality embeddings and FAISS for lightning-fast similarity searches across document chunks.
* **Modular & Portable:** The RAG component is designed as a self-contained microservice, deployed independently via its own Docker setup, showcasing a robust modular architecture.
* **User-Friendly API:** Provides a straightforward FastAPI endpoint for querying the RAG system, making it easy to integrate into other applications.

---

##  Development Setup & Considerations

* **Local Development:** The setup uses lightweight SQLite for Airflow and Docker volumes for persistent storage of logs, model files, and the FAISS index, facilitating easy local development and quick iteration.
* **Production Scalability:** For production environments, the setup is designed to be easily upgraded by replacing SQLite with PostgreSQL and adopting a CeleryExecutor for Airflow, enabling distributed task execution.
* **Containerization Strategy:** Docker Compose orchestrates all services, ensuring a consistent and isolated environment across different machines. The RAG component's self-contained Docker setup within its subdirectory exemplifies best practices for microservice deployment.

---

##  Key Project Paths

ML_LLM_Pipeline/
├── airflow/                 # Airflow DAGs for orchestrating ML workflows
├── api/                     # FastAPI application for ML model inference
├── data/                    # Shared input data (e.g., WineQuality.csv)
├── models/                  # Stores trained ML models (e.g., model.pkl)
├── mlruns/                  # MLflow tracking server data and experiment logs
├── rag/                     # LLM + FAISS RAG system code and its independent Docker setup
├── scripts/                 # PySpark training script for ML pipeline
└── docker-compose.yml       # Main Docker Compose for the core ML pipeline services

---

##  Project Status

* **Part A: ML Pipeline:** Fully functional and automated end-to-end, leveraging Docker, MLflow, FastAPI, and Airflow for a complete MLOps experience.
* **Part B: RAG-style LLM Pipeline:** Successfully implemented, robustly containerized, and deployed as a modular, independent service for contextualized AI queries.

This project stands as a testament to building robust, scalable, and intelligent systems using a modern MLOps toolchain.
