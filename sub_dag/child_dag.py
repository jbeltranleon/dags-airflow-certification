import base64
import requests

from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import PythonOperator


@task.python(multiple_outputs=True)
def get_response():
    return requests.get('https://jsonplaceholder.typicode.com/todos/1').json()


def _encode_title(ti):
    title = ti.xcom_pull(key="title", task_ids="get_response")

    title_bytes = title.encode('ascii')
    base64_bytes = base64.b64encode(title_bytes)
    base64_title = base64_bytes.decode('ascii')
    return base64_title


def _set_username(ti):
    uid = ti.xcom_pull(key="userId", task_ids="get_response")
    usernames = {1: 'Bob'}
    return usernames.get(uid)


def _build_file(ti):
    completed = ti.xcom_pull(key="completed", task_ids="get_response")
    encoded_title = ti.xcom_pull(task_ids="encode_title")
    username = ti.xcom_pull(task_ids="set_username")

    with open(file='file.csv', mode='w') as f:
        f.write(f"username, encoded_title, completed\n{username},{encoded_title},{completed}")


def subdag_factory(parent_dag_id, subdag_dag_id, default_args):
    with DAG(dag_id=f"{parent_dag_id}.{subdag_dag_id}", default_args=default_args) as dag:
        encode_title = PythonOperator(task_id="encode_title", python_callable=_encode_title)
        set_username = PythonOperator(task_id="set_username", python_callable=_set_username)
        build_file = PythonOperator(task_id="build_file", python_callable=_build_file)

        get_response() >> [encode_title, set_username] >> build_file

    return dag
