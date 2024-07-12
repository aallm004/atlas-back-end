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
        employee_info = json.loads(response.read().decode())
    with urllib.request.urlopen(employee_url) as response:
        todo_list = response.read().json()
    employee_name = employee_info['username']

    completed_todo = [x["title"] for x in todo_list if x["completed"]]
    total_todo = len(todo_list)
    total_complete = len(completed_todo)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, total_complete, total_todo))

    csv_file_name = f"{employee_id}.csv"
    with open(f'{employee_id}.csv', 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todo_list:
            writer.writerow([employee_id, employee_name,
                             completed_todo, todo_list])

    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    get_employee_todo_progress(int(sys.argv[1]))
