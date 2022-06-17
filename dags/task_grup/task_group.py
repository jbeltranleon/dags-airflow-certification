import requests
import base64

from datetime import timedelta, datetime

from airflow import DAG
from airflow.decorators import task
from airflow.utils.task_group import TaskGroup

default_args = {"start_date": datetime(2022, 1, 7)}


@task.python(multiple_outputs=True)
def get_response():
    return requests.get('https://jsonplaceholder.typicode.com/todos/1').json()


@task.python
def encode_title(title):
    title_bytes = title.encode('ascii')
    base64_bytes = base64.b64encode(title_bytes)
    base64_title = base64_bytes.decode('ascii')
    return base64_title


@task.python
def set_username(uid):
    usernames = {1: 'Bob'}
    return usernames.get(uid)


@task.python
def build_file(encoded_title, username, completed=False):
    with open(file='file.csv', mode='w') as f:
        f.write(f"username, encoded_title, completed\n{username},{encoded_title},{completed}")


@task.python
def read_file():
    with open(file='file.csv', mode='r') as f:
        for line in f.readlines():
            print(line)


with DAG(dag_id="task_group", description="Main Dag - Tasks Group example", dagrun_timeout=timedelta(minutes=10),
         default_args=default_args) as dag:

    with TaskGroup(group_id="process") as transform:

        response = get_response()

        build_file(encoded_title=encode_title(response["title"]),
                   username=set_username(response["userId"]))

    transform >> read_file()
