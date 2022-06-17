# If the file contains the words airflow or dag, the scheduler will try to load the file
from airflow import DAG
from datetime import datetime, timedelta

from airflow.decorators import task, dag
from airflow.models import Variable
from airflow.operators.python import PythonOperator

# Do not get variables outside a function, this creates a lot of useless connections (affect db)
# variable = Variable.get("my_dag_variable")


@task.python
def extract():
    # variable = Variable.get("my_dag_variable")
    # Use dicts instead of generating individual variables
    settings = Variable.get("my_dag_settings", deserialize_json=True)
    email = settings.get("email")
    hobbies = settings.get("hobbies")
    secret = Variable.get("my_dag_secret")
    print(email, secret, hobbies[0])


def _extract_using_template(*values):
    for value in values:
        print(f"Value: {value}")


def _set_xcom():
    message = "Hi Python"
    # ti.xcom_push(key="message", value=message)
    # Alternative method to push values to xcom
    return message


def _get_xcom(ti):
    # message = ti.xcom_pull(key="message", task_ids="set_xcom")
    # Alternative method to pull values to xcom (key="return_value" optional)
    message = ti.xcom_pull(task_ids="set_xcom")
    print(message)


"""
@dag(description="DAG in charge of ... *This allow Markdown*", start_date=datetime(2021, 11, 4),
     schedule_interval=None, dagrun_timeout=timedelta(minutes=10), tags=["data_science"], catchup=False)
def my_dag():
"""
with DAG(dag_id="my_dag", description="DAG in charge of ... *This allow Markdown*", start_date=datetime(2021, 11, 4),
         schedule_interval=None, dagrun_timeout=timedelta(minutes=10), tags=["data_science"], catchup=False) as dag:

    # Do not get variables outside a function, this creates a lot of useless connections (affect db)
    # variable = Variable.get("my_dag_variable")

    extract_using_template = PythonOperator(task_id="extract_using_template", python_callable=_extract_using_template,
                                            op_args=["{{var.json.my_dag_settings.email}}"])

    extract_using_template_and_env_var = PythonOperator(task_id="extract_using_template_and_env_var",
                                                        python_callable=_extract_using_template,
                                                        op_args=["{{var.json.my_dag_important_number}}"])

    set_xcom = PythonOperator(task_id="set_xcom", python_callable=_set_xcom)
    get_xcom = PythonOperator(task_id="get_xcom", python_callable=_get_xcom)

    get_data_using_ds = PythonOperator(task_id='get_ds', python_callable=_extract_using_template,
                                       op_args=["{{ts}}", "{{ds}}", "{{run_id}}"])

    extract() >> extract_using_template >> extract_using_template_and_env_var >> get_data_using_ds
    get_data_using_ds >> set_xcom >> get_xcom

"""
# Required using the @dag decorator
my_dag()
"""
