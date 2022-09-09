#!/usr/bin/python3
"""
    Export to CSV
    Using what you did in the task #0,
    extend your Python script to export data in the CSV format.
"""

import csv
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

        with open(id + '.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_ALL)
            for task in json_todo:
                TASK_COMPLETED_STATUS = task.get('completed')
                TASK_TITLE = task.get('title')
                csv_writer.writerow([USER_ID,
                                    USERNAME,
                                    TASK_COMPLETED_STATUS,
                                    TASK_TITLE])
