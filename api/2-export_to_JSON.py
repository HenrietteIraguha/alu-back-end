#!/usr/bin/python3
"""Script that exports employee TODO list data to a JSON file."""
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{base_url}/users/{employee_id}").json()
    todos = requests.get(
        f"{base_url}/todos", params={"userId": employee_id}).json()

    username = user.get("username")
    filename = f"{employee_id}.json"

    tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        for task in todos
    ]

    with open(filename, mode='w') as jsonfile:
        json.dump({str(employee_id): tasks}, jsonfile)
