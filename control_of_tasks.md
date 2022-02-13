# Control of Tasks

## Instance level

```python
paralelism = 32 # This variable controls the number of task instances that the airflow worker can run simultaneously. User could increase the parallelism variable in the airflow.cfg
dag_concurrency = 16 # The Airflow scheduler will run no more than $concurrency task instances for your DAG at any given time. Concurrency is defined in your Airflow DAG. If you do not set the concurrency on your DAG, the scheduler will use the default value from the dag_concurrency entry in your airflow.cfg
max_active_runs_per_dag = 16 # the Airflow scheduler will run no more than max_active_runs DagRuns of your DAG at a given time. If you do not set the max_active_runs in your DAG, the scheduler will use the default value from the max_active_runs_per_dag entry in your airflow.cfg
```

## DAG level

```python
concurrency = 16 # The Airflow scheduler will run no more than $concurrency task instances for your DAG at any given time. Concurrency is defined in your Airflow DAG
max_active_runs = 16 # the Airflow scheduler will run no more than max_active_runs DagRuns of your DAG at a given time
```

## Task level

```python
task_concurrency = 1 # This variable controls the number of concurrent running task instances across dag_runs per task
pool = 'default_pool' # This variable controls the number of concurrent running task instances assigned to the pool.
```

> You could create pools using the UI and then defining the poll's slots for example to 1 and then asign the pool name on the DAG's pool argument. This is helpful if you want to limit parallel task that consumes more resources.
> Use `pool_slots` to define how many slots the task could take


# Priority

Use `priority_weigth` to define the task's priority when the task is executed in parallel with others.
> The larger the number the higher the priority. The priority is evaluated at the pool level