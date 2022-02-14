# Timeout

## DAG level

* `dag_run_timeout=timedelta(minutes=10)` to avoid deadlock. Only works for scheduled times

# Task level

* `execution_timeout=timedelta(minutes=10)` this value has not a default value