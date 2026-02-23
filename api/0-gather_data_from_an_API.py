#!/usr/bin/python3
"""Script that returns information about an employee's TODO list progress."""
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{base_url}/users/{employee_id}").json()
    todos = requests.get(
        f"{base_url}/todos", params={"userId": employee_id}).json()

    name = user.get("name")
    done = [t for t in todos if t.get("completed")]
    total = len(todos)
    num_done = len(done)

    print(f"Employee {name} is done with tasks({num_done}/{total}):")
    for task in done:
        print(f"\t {task.get('title')}")
