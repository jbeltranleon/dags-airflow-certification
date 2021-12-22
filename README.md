# Airflow Certification Course

## Defining a DAG
* Use with `Dag(...) as dag:` avoiding `dag=dag`
* Using same `dag_id` in more that one DAGs, the UI Will display one of them randomly
* Each task could have its own start_date...
* Using timedelta instead of cron expression the process will calculate the start time base on the time when the scheduler found the file
* dagrun_timeout fail if the dag take X time
* catchup default True (Ponerse al día)

> The DAG [X] starts being scheduled from the start_date and will be 
triggered after every schedule_interval

## Cron vs Timedelta

**Cron expression** is stateless, **Timedelta** is stateful or relative (according to the last execution date)

> Timedelta is useful for every three days executions

DAG: `processor_customer`

```python
start_date=datetime(2021, 1, 1, 10, 0) # 01-01-2021 10:00
# A) first execution: 02-01-2021 00:00
schedule_interval = '0 0 * * *' #'@daily'
# B) first execution: 02-01-2021 10:00
schedule_interval = timedelta(days=1)
```

## Task idempotence and determinism

**Idempotence:** If you execute you task multiple times, it will always produce the same side effect

**Determinism:** If you execute your task, for the same input you will always get the same output

## Backfilling

Use start_date and catchup to backfill previous executions. Or use this command to backfill dags even if the catchup is set to false:

`airflow dags backfill -s 2020-01-01 -e 2021-01-01`

and add the parameter `max_active_runs` to the dag definition for a better backfilling handle.

## Test

To test specific task using a cli command: `airflow tasks test my_dag extract 2021-01-01`