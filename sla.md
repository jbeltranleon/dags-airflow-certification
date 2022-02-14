# SLA

## Definition

1. At the DAG level

* `sla_miss_callback=_callback_function` defined at the dag level

```python
def _callback_function(dag, task_list, blocking_task_list, slas, blocking_tis):
    pass
```

2. At the Task level

* `sla=timedelta(minutes=5)` Based on the execution date of the DAG


> useful on the last task, the sla doesn't work on manual execution

> require the SMTP configuration