#!/usr/bin/python3
"""
Python script that returns info about his/her TODO list progress
"""
import json
from flask import request
import sys
import urllib.request


def fetch_employee_tasks():
    api_url = "https://your-api-endpoint.com/tasks"
    response = requests.get(api_url)
    tasks_data = response.json()
    return tasks_data


def organize_tasks_by_user(tasks_data):
    user_tasks = {}
    for task in tasks_data:
        user_id = task["user_id"]
        username = task["username"]
        task_title = task["task_title"]
        completed = task["completed"]

        if user_id not in user_tasks:
            user_tasks[user_id] = []

        user_tasks[user_id].append({
            "username": username,
            "task": task_title,
            "completed": completed
        })

    return user_tasks


def save_to_json(user_tasks).
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(user_tasks, json_file, indent=4)


if __name__ == "__main__":
    tasks_data = fetch_employee_tasks()
    user_tasks = organize_tasks_by_user(tasks_data)
    save_to_json(user_tasks)
    print("Data exported to todo_all_employees.json")
