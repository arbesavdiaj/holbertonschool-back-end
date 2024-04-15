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
    print(user)

    response = requests.get(base_url + 'todos/')
    if response.status_code != 200:
        return print("Error", response.status_code)
    todos = response.json()

    user_todos = [todo for todo in todos if todo.get('userId') == user.get('id')]
    completed = [todo for todo in user_todos if todo.get('completed')]
    
    total_tasks = len(user_todos)
    done_tasks = len(completed)

    print(f"Employee {user['name']} is done with tasks ({done_tasks}/{total_tasks}):")
    for task in completed:
        print("\t", task)


if __name__ == "__main__":
    do_request()
