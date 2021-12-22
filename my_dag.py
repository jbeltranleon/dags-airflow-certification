# If the file contains the words airflow or dag, the scheduler will try to load the file
from airflow import DAG
from datetime import datetime, timedelta
from airflow.models import Variable
from airflow.operators.python import PythonOperator


def _extract():
    variable = Variable.get('my_dag_variable')
    secret = Variable.get('my_dag_secret')

    print(variable, secret)


with DAG(dag_id="my_dag", description="DAG in charge of ... *This allow Markdown*", start_date=datetime(2021, 11, 4),
         schedule_interval="@daily", dagrun_timeout=timedelta(minutes=10), tags=["data_science"], catchup=False) as dag:

    extract = PythonOperator(task_id="extract", python_callable=_extract)
