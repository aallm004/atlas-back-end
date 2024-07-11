#!/usr/bin/python3
"""
Python script that returns info about his/her TODO list progress
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    
    try:
        user_response = requests.get(api_url)
        todos_response = requests.get(todo_url)
        
        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_data.get("name")
        total_tasks = len(todos_data)
        done_tasks = sum(1 for todo in todos_data.get if todo.get("completed"))

        print(f"Employee: {employee_name} is done with tasks \
              ({done_tasks}/{total_tasks}):")
        print(f"{employee_name}: {done_tasks} completed tasks")
        print(f"Total tasks: {total_tasks}")

        for todo in todos_data:
            if todo.get("completed"):
                print(f"{todo.get('title')}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

    if len(sys.argv) > 1:
        print("Incorrect, not <employee_id>")
        sys.exit(1)
