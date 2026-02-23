#!/usr/bin/python3
"""Script that exports all employees TODO list data to a JSON file."""
import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users = requests.get(f"{base_url}/users").json()
    todos = requests.get(f"{base_url}/todos").json()

    all_tasks = {}

    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")
        all_tasks[user_id] = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos if task.get("userId") == user.get("id")
        ]

    with open("todo_all_employees.json", mode='w') as jsonfile:
        json.dump(all_tasks, jsonfile)
