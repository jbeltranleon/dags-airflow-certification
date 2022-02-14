# Trigger DAG run Operator

> It is not a sensor

```python

from airflow.operators.trigger_dagrun import TriggerDagRunOperator

cleaning_xcoms = TriggerDagRunOperator(task_id='cleaning',
                                       trigger_dag_id='external_dag',
                                       execution_date='{{ds}}',
                                       wait_for_completion=True,
                                       poke_interval=60,
                                       reset_dag_run=True,
                                       failed_states=['failed'])

```