# Callbacks

## DAG level

* `on_success_callback=_success_callback`
```python
def _success_callback(context):
    pass
```
* `on_failure_callback=_failure_callback`
```python
from airflow.exceptions import AirflowTaskTimeout, AirflowSensorTimeout
def _failure_callback(context):
    if context.get('exception'):
        if isinstance(context.get('exception'), AirflowTaskTimeout):
            pass
        if isinstance(context.get('exception'), AirflowSensorTimeout):
            pass
```

## Task level

* `on_success_callback`
* `on_failure_callback`
* `on_retry_callback`
```python
def _retry_callback(context):
    if context.get('ti').try_number() > 2:
        pass
```
