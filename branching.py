from datetime import datetime, timedelta
from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import BranchPythonOperator


@task.python()
def task_a():
    print('task a')


@task.python()
def task_b():
    print('task b')


@task.python
def task_c():
    print('task c')


@task.python(trigger_rule='none_failed_or_skipped')
def task_d():
    print('task d')


def _branching_task():
    if datetime.now().day % 2 == 0:
        return 'task_b'
    return 'task_c'


with DAG(dag_id="branching_example", description="Branching", start_date=datetime(2022, 2, 7), schedule_interval=None,
     dagrun_timeout=timedelta(minutes=10), tags=["test"], catchup=False) as dag:

    branching_task = BranchPythonOperator(
        task_id='branching_task',
        python_callable=_branching_task)

    task_a() >> branching_task >> [task_b(), task_c()] >> task_d()
