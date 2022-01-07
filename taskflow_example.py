from datetime import datetime, timedelta

from airflow.decorators import task, dag


@task.python
def set_xcom():
    message = "Hi Python"
    return message


@task.python
def get_xcom(message):
    print(message)


@dag(description="DAG Description", start_date=datetime(2021, 11, 4), schedule_interval=None,
     dagrun_timeout=timedelta(minutes=10), tags=["test"], catchup=False)
def task_flow_example_dag():
    get_xcom(set_xcom())


# Required using the @dag decorator
task_flow_example_dag()
