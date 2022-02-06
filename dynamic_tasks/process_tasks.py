import requests

from airflow.utils.task_group import TaskGroup
from airflow.decorators import task


@task.python(multiple_outputs=True)
def get_response(user_id):
    return requests.get(f'https://jsonplaceholder.typicode.com/todos/{user_id}').json()


@task.python
def build_file(user_id, title, name, username, email):
    with open(file=f'{username}.csv', mode='w') as f:
        f.write(f"username, encoded_title, name, username, email\n{user_id},{title},{name}, {username}, {email}")


def process_tasks(user_id, name, username, email):
    with TaskGroup(group_id=f"process_{username}") as transform:
        response = get_response(user_id)
        build_file(user_id, response["title"], name, username, email)

    return transform
