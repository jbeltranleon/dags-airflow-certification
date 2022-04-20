import requests

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
# https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/operators/s3.html
from airflow.hooks.S3_hook import S3Hook
from airflow.operators.bash import BashOperator


def _upload_file_to_s3(filename: str, key: str, bucket_name: str):
    hook = S3Hook('s3_conn')
    hook.load_file(filename=filename, key=key, bucket_name=bucket_name)


with DAG(
        dag_id="second_challenge_bash",
        description="Second Challenge Upload S3",
        start_date=datetime(2022, 3, 24),
        schedule_interval=None,
        dagrun_timeout=timedelta(minutes=10),
        tags=["study_group", "challenge"],
        catchup=False
) as dag:
    save_api_response_bash = BashOperator(
        task_id="save_api_response_bash",
        bash_command="// Add code here"
    )

    upload_file_to_s3 = PythonOperator(
        task_id="upload_file_to_s3",
        python_callable=_upload_file_to_s3,
        op_kwargs={
            'filename': './file.csv',
            'key': 'file_from_airflow_bash.csv',
            'bucket_name': 'factored-airflow-study-group'
        }
    )

    save_api_response_bash >> upload_file_to_s3
