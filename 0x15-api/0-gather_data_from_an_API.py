#!/usr/bin/python3
"""
    Gather data from an API
"""

from requests import get
from sys import argv, exit

if __name__ == "__main__":
    try:
        id = argv[1]
        is_integer = int(id)
    except Exception:
        exit()

    url = "https://jsonplaceholder.typicode.com/"
    url_user = url + "users?id=" + id
    url_todo = url + "todos?userId=" + id

    request_user = get(url_user)
    request_todo = get(url_todo)
    try:
        json_user = request_user.json()
        json_todo = request_todo.json()
    except ValueError:
        print("No Json")

    if json_user and json_todo:
        EMPLOYEE_NAME = json_user[0].get('name')
        NUMBER_OF_DONE_TASKS = 0
        for task in json_todo:
            if task.get('completed'):
                NUMBER_OF_DONE_TASKS += 1
        TOTAL_NUMBER_OF_TASKS = len(json_todo)

        print("Employee {} is done with tasks({}/{}):"
              .format(EMPLOYEE_NAME,
                      NUMBER_OF_DONE_TASKS,
                      TOTAL_NUMBER_OF_TASKS))

        for doing in json_todo:
            TASK_TITLE = doing.get('title')
            if doing.get('completed'):
                print("\t {}".format(TASK_TITLE))
