#!/usr/bin/python3
"""
Python script that returns info about his/her TODO list progress
"""
import csv
import json
import sys
import urllib.request


def get_employee_todo_progress(employee_id):

    base_url = "https://jsonplaceholder.typicode.com/"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    with urllib.request.urlopen(employee_url) as response:
        employee_info = response.read().json()
    with urllib.request.urlopen(employee_url) as response:
        todo_list = response.read().json()
    employee_name = employee_info['username']

    completed_todo = [x["title"] for x in todo_list if x["completed"]]
    total_todo = len(todo_list)
    total_complete = len(completed_todo)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, total_complete, total_todo))

    with open(f'{employee_id}.csv', 'w') as f:
        for todo in todo_list:
            x = f'"{employee_id}",' + \
                f'"{employee_name}",' + \
                f'"{completed_todo}",' + \
                f'"{todo_list}"'

            f.write(x)


if __name__ == "__main__":
    get_employee_todo_progress(int(sys.argv[1]))
