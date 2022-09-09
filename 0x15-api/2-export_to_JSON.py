#!/usr/bin/python3
"""
    Export to JSON
    Using what you did in the task #0,
    extend your Python script to export data in the JSON format.
"""

import json
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
        USER_ID = id
        USERNAME = json_user[0].get('username')

        json_list = []
        for task in json_todo:
            TASK_TITLE = task.get('title')
            TASK_COMPLETED_STATUS = task.get('completed')
            taskdict = {"task": TASK_TITLE,
                        "completed": TASK_COMPLETED_STATUS,
                        "username": USERNAME}
            json_list.append(taskdict)

        json_result = {USER_ID: json_list}

        with open(id + '.json', 'w', newline='') as json_file:
            json.dump(json_result, json_file)