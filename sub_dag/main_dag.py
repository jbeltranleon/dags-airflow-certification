import requests

from datetime import timedelta, datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.subdag import SubDagOperator

from dags.sub_dag.child_dag import subdag_factory

default_args = {"start_date": datetime(2022, 1, 7)}


@task.python(multiple_outputs=True)
def get_response():
    return requests.get('https://jsonplaceholder.typicode.com/todos/1').json()


@task.python
def read_file():
    with open(file='file.csv', mode='r') as f:
        for line in f.readlines():
            print(line)


with DAG(dag_id="main", description="Main Dag - SubDag example", dagrun_timeout=timedelta(minutes=10),
         default_args=default_args) as dag:

    transform = SubDagOperator(
        task_id="process",
        subdag=subdag_factory(parent_dag_id="main", subdag_dag_id="process", default_args=default_args),
        poke_interval=3
    )

    get_response() >> transform >> read_file()
