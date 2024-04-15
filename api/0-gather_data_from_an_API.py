#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""


import requests
import sys


def get_employee_todo_list_progress(employee_id):
    # Get the employee details
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee = requests.get(url).json()

    # Get the employee's TODOs
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    todos = requests.get(url).json()

    # Calculate the progress
    total_tasks = len(todos)
    done_tasks = len([todo for todo in todos if todo['completed']])
    employee_name = employee['name']

    # Print the progress
    progress_info = (f'Employee {employee_name} is done with '
                     f'tasks({done_tasks}/{total_tasks}):')
    print(progress_info)
    for todo in todos:
        if todo['completed']:
            print('\t ' + todo['title'])


if __name__ == "__main__":
    get_employee_todo_list_progress(int(sys.argv[1]))
