from datetime import datetime
from unittest import mock

from airflow.operators.python import PythonOperator

from dags.exchange_dag import _upload_file_to_s3


def test_upload_file_to_s3_should_call_load_fule_once():
    with mock.patch("airflow.hooks.S3_hook.S3Hook.load_file") as mock_load_file:
        mock_load_file.return_value = None
        test = PythonOperator(task_id="test",
                              python_callable=_upload_file_to_s3,
                              op_kwargs={
                                  'filename': './file.csv',
                                  'key': 'exe.csv',
                                  'bucket_name': 'factored-airflow-study-group'
                              })
        test.execute(context={"execution_date": datetime(2021, 1, 1)})
        mock_load_file.assert_called_once()
