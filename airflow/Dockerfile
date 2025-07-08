FROM apache/airflow:2.9.1-python3.10

USER root
# Optional: install OS-level packages here (like apt-get), then switch back
# RUN apt-get update && apt-get install -y <your-system-packages-if-needed>

USER airflow
RUN pip install --no-cache-dir pandas scikit-learn joblib
