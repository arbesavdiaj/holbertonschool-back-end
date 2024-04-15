#!/usr/bin/python3
import requests
import sys


base_url = 'https://jsonplaceholder.typicode.com/'


def do_request():
    if len(sys.argv) < 2:
        print("correct usage", __file__, "<employee_id>")

    eid = sys.argv[1]

    response = requests.get(base_url + 'users/' + eid)
    if response.status_code == 404:
        return print("Error...")
    if response.status_code != 200:
        return print("Error with code", response.status_code)
    user = response.json()

    response = requests.get(base_url + 'todos/')
    if response.status_code != 200:
        return print("Error", response.status_code)
    todos = response.json()

    user_todos = []
    for todo in todos:
        if todo.get('userId') == user.get('id'):
            user_todos.append(todo)

    completed = [todo for todo in user_todos if todo.get('completed')]

    for task in completed:
        print(task)

    if __name__ == "__main__":
        do_request()
