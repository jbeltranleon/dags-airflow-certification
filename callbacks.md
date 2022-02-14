# Callbacks

## DAG level

* `on_success_callback=_success_callback`
```python
def _success_callback(context):
    pass
```
* `on_failure_callback=_failure_callback`

## Task level

* `on_success_callback`
* `on_failure_callback`
* `on_retry_callback`
