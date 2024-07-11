#!/usr/bin/python3

import requests
import sys


def get_employee_todo_progress(employee_id):
    api_url = f"https://jsonplaceholder.typicode.com/"

    try:
        response = requests.get(api_url)
        response_data = response.json()

        employee_name = response_data.get("employee_name")
        total_tasks = len(response_data.get("todos"))
        done_tasks = sum(1 for todo in response_data.get("todos") if todo.get("status") == "Done")

        print(f"Employee: {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
        print(f"{employee_name}: {done_tasks} completed tasks")
        print(f"Total tasks: {total_tasks}")

        for todo in response_data.get("todos"):
            if todo.get("status") == "Done":
                print(f"\t{todo.get('title')}")
        
    except requests.RequestException as e:
        print(f"Error fethcing data: {e}")

    if len(sys.argv) > 1:
        print("Incorrect, not <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_todo_progress(employee_id)
