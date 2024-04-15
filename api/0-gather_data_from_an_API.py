#!/usr/bin/python3
"""
Model to make a request to an
API and retrieve data
"""


import json
import requests
from sys import argv


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    res = requests.get(f"{URL}users/{argv[1]}")
    res = res.json()
    user_name = res['name']

    res = requests.get(f"{URL}todos")
    all_todos = res.json()
    user_todos = [todo for todo in all_todos if todo['userId'] == int(argv[1])]
    nr_tasks = len(user_todos)
    completed_tasks = [completed for completed in user_todos
                       if completed['completed'] is True]
    completed_title = [title['title'] for title in completed_tasks]

    print(f"Employee {user_name} is done", end="")
    print(f" with tasks({len(completed_tasks)}/{nr_tasks}):")
    for title in completed_title:
        print(f"\t {title}")
