#!/usr/bin/python3
"""
    Dictionary of list of dictionaries
    Using what you did in the task #0,
    extend your Python script to export data in the JSON format.
"""

import json
from requests import get

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    url_user = url + "users"
    url_todo = url + "todos"

    request_user = get(url_user)
    request_todo = get(url_todo)
    try:
        json_user = request_user.json()
        json_todo = request_todo.json()
    except ValueError:
        print("No Json")

    if json_user and json_todo:
        json_re = {}
        user_names = {}
        for user in json_user:
            USER_ID = user.get('id')
            USERNAME = user.get('username')
            json_re[USER_ID] = []
            user_names[USER_ID] = USERNAME

        for task in json_todo:
            TASK_TITLE = task.get('title')
            TASK_COMPLETED_STATUS = task.get('completed')
            user_id = task.get("userId")
            taskdict = {"task": TASK_TITLE,
                        "completed": TASK_COMPLETED_STATUS,
                        "username": user_names.get(user_id)}

            if json_re.get(user_id) is not None:
                json_re.get(user_id).append(taskdict)

        with open('todo_all_employees.json', 'w', newline='') as jsonfile:
            json.dump(json_re, jsonfile)
