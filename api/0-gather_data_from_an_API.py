#!/usr/bin/python3
"""
Python script that returns info about his/her TODO list progress
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    
    api_url = "https://jsonplaceholder.typicode.com/"
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos"


    employee_info = requests.get("employ_url").json()
    employee_name = employee_info.get("name")
    todo_list = requests.get(todo_url, p={"userId": employee_id}).json()

    completed_todo = [x["title"] for x in todo_list if x["completed"]]
    total_todo = len(todo_list)
    total_complete = len(completed_todo)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, total_complete, total_todo))

    for todo in completed_todo:
        print("\t {}".format(todo))

if __name__ == "__main__":
    get_employee_todo_progress(int(sys.argv[1]))
