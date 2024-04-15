#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""


import json
import requests
from sys import argv


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    data = requests.get(f"{URL}users/{argv[1]}")
    data = data.json()
    user_name = data['name']

    data = requests.get(f"{URL}todos")
    all_todos = data.json()
    user_todos = [todo for todo in all_todos if todo['userId'] == int(argv[1])]
    nr_tasks = len(user_todos)
    comp_tasks = [comp for comp in user_todos if comp['completed'] is True]
    comp_title = [title['title'] for title in comp_tasks]

    print(f"Employee {user_name} is done", end="")
    print(f" with tasks({len(comp_tasks)}/{nr_tasks}):")
    for title in comp_title:
        print(f"\t {title}")
