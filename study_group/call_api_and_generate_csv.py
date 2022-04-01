import requests

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


def _save_api_response():
    # Error with response.json
    # response = requests.get('https://www.boredapi.com/')
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
        dag_id="fist_challenge",
        description="Call an API, generate CSV file with the response and upload the file to a SFTP",
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

    save_api_response_bash = BashOperator(
        task_id="save_api_response_bash",
        bash_command="curl https://www.boredapi.com/api/activity/ > ./file_2.csv"
    )

    upload_file_to_sftp = PythonOperator(
        task_id="upload_file_to_sftp",
        python_callable=_upload_file_to_sftp
    )

    [save_api_response, save_api_response_bash] >> upload_file_to_sftp
