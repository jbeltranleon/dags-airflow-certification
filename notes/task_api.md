# TaskFlow API

## Decorators

``` python
@task.python # Airflow create the airflow operator
@task.virtualenv # Exec python func within python env
@task.group # Group of tasks
```

> Create Dags faster

## XCOM ARGS

> Define dependencies between tasks explicitly