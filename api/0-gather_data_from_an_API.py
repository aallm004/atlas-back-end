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

    employee_info = requests.get(employee_url).json()
    employee_name = employee_info['name']
    todo_list = requests.get(todo_url, params={"userId": employee_id}).json()

    completed_todo = [x["title"] for x in todo_list if
                      x["completed"]]
    total_todo = len(todo_list)
    total_complete = len(completed_todo)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, total_complete, total_todo))

    for todo in completed_todo:
        print(f"\t {todo}")

    if __name__ == "__main__":
        get_employee_todo_progress(int(sys.argv[1]))
