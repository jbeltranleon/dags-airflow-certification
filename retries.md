# Retries

## DAGS or Task level

* `retries` default 0

The argument at the task overwrite the value of the value defined at the DAG definition

* `retry_delay=timedelta(minutes=5)`
* `retry_exponential_backoff=True` Helpful for API or DB communication
* `max_retry_delay=timedelta(minutes=15)`

