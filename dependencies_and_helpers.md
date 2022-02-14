# Dependencies and Helpers

## Defining dependencies

### Old way

Using the `set_upstream` and `set_downstream` functions

```python
t2.set_upstream(t1)
t1.set_downstream(t2)
```

### Actual way

```python
t2 << t1
t1 >> t2
```

> We can not create dependencies between two lists
 
`[t1, t2] >> [t3, t4] # TypeError: unsupported...`

### Creating cross dependencies

`cross_downstream` doesn't return values, so you can't add new tasks after that fuction

```python
from airflow.models.baseoperator import cross_downstream

cross_downstream([t1, t2], [t3, t4])

# next task
[t3, t4] >> t5

```

### Chain Dependencies

Both lists should have the same len

```python
from airflow.models.baseoperator import chain

chain(t1, [t2, t3], [t4, t5], t6)
```