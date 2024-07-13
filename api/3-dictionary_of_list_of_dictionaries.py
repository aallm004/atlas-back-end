#!/usr/bin/python3
"""
Python script that exports all tasks from all employees in JSON format
"""
import json
import sys
import urllib.request


def get_all_employee_todo_progress():
    base_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = "https://jsonplaceholder.typicode.com/todos"

    with urllib.request.urlopen(base_url) as response:
        employees = json.loads(response.read())

    with urllib.request.urlopen(todo_url) as response:
        todo_list = json.loads(response.read())

    all_employees_tasks = {}

    for employee in employees:
        employee_id = employee["id"]
        employee_name = employee["name"]
        employee_tasks = []

        for todo in todo_list:
            if todo["userId"] == employee_id:
                task_info = {
                    "username": employee_name,
                    "task": todo["title"],
                    "completed": todo["completed"]
                }
                employee_tasks.append(task_info)

        all_employees_tasks[employee_id] = employee_tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_employees_tasks, json_file, indent=2)

    print(f"Data exported to todo_all_employees.json")


if __name__ == "__main__":
    get_all_employee_todo_progress()
