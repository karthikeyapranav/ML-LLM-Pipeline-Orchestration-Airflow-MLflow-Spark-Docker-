# dags/ml_pipeline_dag.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
sys.path.append("/opt/airflow/scripts")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    dag_id="ml_pipeline_wine",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
)

from scripts.data_ingestion import ingest_data
from scripts.feature_engineering import feature_engineer
from scripts.model_training import train
from scripts.model_evaluation import evaluate

t1 = PythonOperator(task_id='data_ingestion', python_callable=ingest_data, dag=dag)
t2 = PythonOperator(task_id='feature_engineering', python_callable=feature_engineer, dag=dag)
t3 = PythonOperator(task_id='model_training', python_callable=train, dag=dag)
t4 = PythonOperator(task_id='model_evaluation', python_callable=evaluate, dag=dag)

t1 >> t2 >> t3 >> t4
