# If the file contains the words airflow or dag, the scheduler will try to load the file
from airflow import DAG
from datetime import datetime, timedelta

# Use with Dag(...) as dag: avoiding dag=dag
# Using same dag_id the UI Will display one of them randomly
# Each task could have its own start_date...

# Using timedelta instead of cron expression the process will calculate the start time base on the time when the
# scheduler found the file
# dagrun_timeout fail if the dag take X time
# catchup default True (Ponerse al día)
from airflow.operators.dummy import DummyOperator

with DAG(dag_id="3_3_getting_started",
         description="Our first DAG. The *UI* displays **this** string with _markdown format_",
         start_date=datetime(2021, 11, 4), schedule_interval="@daily", dagrun_timeout=timedelta(minutes=10),
         tags=["arch", "fundamentals"], catchup=False) as dag:

    # Every Dag's task should have a unique task_id
    start = DummyOperator(
        task_id='start'
    )
