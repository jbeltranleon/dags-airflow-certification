import requests

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
# https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/operators/s3.html
from airflow.providers.amazon.aws.operators.s3 import S3Hook


def _save_api_response():
    response = requests.get('https://www.boredapi.com/api/activity/')
    with open('./file.csv', mode='w') as f:
        if response.json():
            f.write(response.text)


def _upload_file_to_sftp():
    with open('./file.csv', mode='r') as f:
        print(f.readlines())

    with open('./file_2.csv', mode='r') as f:
        print(f.readlines())


with DAG(
        dag_id="second_challenge",
        description="Second Challenge Upload S3",
        start_date=datetime(2022, 3, 24),
        schedule_interval=None,
        dagrun_timeout=timedelta(minutes=10),
        tags=["study_group", "challenge"],
        catchup=False
) as dag:

    save_api_response = PythonOperator(
        task_id="save_api_response",
        python_callable=_save_api_response
    )

    upload_file_to_s3 = PythonOperator(
        task_id="upload_file_to_sftp",
        python_callable=
    )


    save_api_response >> upload_file_to_s3
