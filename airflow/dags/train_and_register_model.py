from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import subprocess

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
}

def run_training_script():
    subprocess.run(["python", "scripts/train_and_register.py"], check=True)

with DAG(
    dag_id='wine_quality_train_and_register',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:
    train_task = PythonOperator(
        task_id='train_and_register',
        python_callable=run_training_script,
    )
