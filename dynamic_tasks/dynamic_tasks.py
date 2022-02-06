from datetime import timedelta, datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.dummy import DummyOperator

from dags.dynamic_tasks.process_tasks import process_tasks
from dags.dynamic_tasks.users import users

default_args = {"start_date": datetime(2022, 1, 7)}


@task.python
def read_file(filename):
    with open(file=f'{filename}.csv', mode='r') as f:
        for line in f.readlines():
            print(line)


with DAG(dag_id="dynamic_tasks", description="Main Dag - Dynamic DAGs example", dagrun_timeout=timedelta(minutes=10),
         default_args=default_args) as dag:

    start = DummyOperator(task_id='start')

    for idx, user in users.items():
        start >> process_tasks(idx, user['name'], user['username'], user['email']) >> read_file(user['username'])
