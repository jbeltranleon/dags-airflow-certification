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

# Cron vs Timedelta
