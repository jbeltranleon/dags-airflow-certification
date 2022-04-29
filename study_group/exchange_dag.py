import requests

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.transfers.s3_to_redshift import S3ToRedshiftOperator
# https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/operators/s3.html
from airflow.hooks.S3_hook import S3Hook


def _save_api_response():
    import pandas as pd

    response = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=20c737f1a0042f2e9df4d1e8e3e7b315&symbols=USD,AUD,CAD,PLN,MXN')
    print(response)
    df = pd.json_normalize(response.json())
    print(df.head())

    df.to_csv('./file.csv', header=False, index=False)


def _upload_file_to_s3(filename: str, key: str, bucket_name: str):
    hook = S3Hook('s3_conn')
    hook.load_file(filename=filename, key=key, bucket_name=bucket_name)


with DAG(
        dag_id="exchange",
        description="Exchange Challenge",
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
        task_id="upload_file_to_s3",
        python_callable=_upload_file_to_s3,
        op_kwargs={
            'filename': './file.csv',
            'key': 'exe.csv',
            'bucket_name': 'factored-airflow-study-group'
        }
    )

    copy_to_redshift = S3ToRedshiftOperator(
        aws_conn_id='s3_conn',
        redshift_conn_id='redshift_conn',
        task_id="copy_to_redshift",
        s3_bucket='factored-airflow-study-group',
        s3_key='exe.csv',
        schema='airflow_sg',
        table='exchange',
        copy_options=['csv']
    )

    save_api_response >> upload_file_to_s3 >> copy_to_redshift
