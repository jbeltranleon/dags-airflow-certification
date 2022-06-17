from datetime import datetime, timedelta
from airflow import DAG
from airflow.decorators import task

from typing import Dict


@task.python(multiple_outputs=True)
def set_xcom():
    message = "Hi Python"
    sender = "jbeltranleon"
    return {"message": message, "sender": sender}


# Same behavior
@task.python(task_id="set_xcom_typed")
def set_xcom_2() -> Dict[str, str]:
    message = "Hi Airflow"
    sender = "jbeltranleon"
    return {"message": message, "sender": sender}


@task.python
def get_xcom(message, sender):
    print(f"{sender}: {message}")


@task.python
def get_xcom_2(message, sender):
    print(f"New message from {sender}: {message}")


with DAG(dag_id="task_flow", description="DAG Description", start_date=datetime(2021, 11, 4), schedule_interval=None,
     dagrun_timeout=timedelta(minutes=10), tags=["test"], catchup=False) as dag:
    values = set_xcom()
    values_2 = set_xcom_2()
    get_xcom(values["sender"], values["message"]) >> get_xcom_2(values_2["sender"], values_2["message"])
