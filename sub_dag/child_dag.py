import base64

from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import get_current_context


@task.python
def encode_title():
    ti = get_current_context()['ti']
    title = ti.xcom_pull(key="title", task_ids="get_response", dag_id="main")

    title_bytes = title.encode('ascii')
    base64_bytes = base64.b64encode(title_bytes)
    base64_title = base64_bytes.decode('ascii')
    return base64_title


@task.python
def set_username():
    ti = get_current_context()['ti']
    uid = ti.xcom_pull(key="userId", task_ids="get_response", dag_id="main")
    usernames = {1: 'Bob'}
    return usernames.get(uid)


@task.python
def build_file():
    ti = get_current_context()['ti']
    completed = ti.xcom_pull(key="completed", task_ids="get_response", dag_id="main")
    encoded_title = ti.xcom_pull(task_ids="encode_title")
    username = ti.xcom_pull(task_ids="set_username")

    with open(file='file.csv', mode='w') as f:
        f.write(f"username, encoded_title, completed\n{username},{encoded_title},{completed}")


def subdag_factory(parent_dag_id, subdag_dag_id, default_args):
    with DAG(dag_id=f"{parent_dag_id}.{subdag_dag_id}", default_args=default_args) as dag:

        [encode_title(), set_username()] >> build_file()

    return dag
