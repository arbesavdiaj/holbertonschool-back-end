#!/usr/bin/python3
"""
Model to make a request to an
API and retrieve data
"""


import json
import requests


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    res = requests.get(f"{URL}users")
    user_data = res.json()

    res = requests.get(f"{URL}todos")
    all_todos = res.json()

    user_json = {}
    for user in user_data:
        user_todos = []
        for todos in all_todos:
            if todos['userId'] == user['id']:
                user_todos.append({"username": user['username'],
                                   "task": todos['title'],
                                   "completed": todos['completed']})
        user_json[f"{user['id']}"] = user_todos

    with open("todo_all_employees.json", 'w') as file:
        json.dump(user_json, file)
