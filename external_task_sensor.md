# External Task Sensor

```python
from airflow.sensors.external_task import ExternalTaskSensor

waiting_for_task = ExternalTaskSensor(task_id='waiting_for_task',
                                      external_dag_id='my_dag',
                                      external_task_ids='my_task',
                                      execution_delta=timedelta(minutes=60),
                                      execution_date_fn=_function_a,
                                      failed_states=['failed', 'skipped'],
                                      allowed_states=['success'])
```