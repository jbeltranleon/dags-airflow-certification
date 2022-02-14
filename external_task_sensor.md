# External Task Sensor

```python
from airflow.sensors.external_task import ExternalTaskSensor

waiting_for_task = ExternalTaskSensor(task_id='waiting_for_task',
                                      external_task_id='my_dag',
                                      external_task_ids='my_task')
```