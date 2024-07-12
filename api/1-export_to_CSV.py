#!/usr/bin/python3
"""
Python script that returns info about his/her TODO list progress
"""
import json
import sys
import urllib.request


if __name__ == "__main__":

    x = ""

    if len(sys.argv) > 1:
        employee_id = int(sys.argv[1])

        base_url = "https://jsonplaceholder.typicode.com/"
        employee_url = f"{base_url}/users/{employee_id}"
        todo_url = f"{base_url}/todos?userId={employee_id}"

        with urllib.request.urlopen(employee_url) as response:
            employee_info = response.read()
        employee_info = json.loads(employee_info)

        with urllib.request.urlopen(todo_url) as response:
            todo_list = response.read()
        todo_list = json.loads(todo_list)

        employee_name = employee_info['name']

        completed_todo = [x["title"] for x in todo_list if x["completed"]]
        total_todo = len(todo_list)
        total_complete = len(completed_todo)

        print("Employee {} is done with tasks({}/{}):"
              .format(employee_name, total_complete, total_todo))

        for todo in todo_list:
            completed = todo['completed']
            title = todo['title']
            x += f'"{employee_id}",' + \
                f'"{employee_name}",' + \
                f'"{completed}",' + \
                f'"{title}"'

        with open(f'{employee_id}.csv', 'w') as f:
            f.write(x)

    else:
        print("Usage: 1-export_to_CSV.py <employee_id>")
