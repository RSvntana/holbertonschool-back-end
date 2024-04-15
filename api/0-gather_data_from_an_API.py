#!/usr/bin/python3
"""Retrieves and displays an employee's TODO list progress"""
import requests
import sys


def get_employee_todos(employee_id):
    """Retrieves the employee's todos from the API"""
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    todos = response.json()
    return todos


def display_todo_progress(employee_id):
    """Displays the employee's TODO list progress"""
    todos = get_employee_todos(employee_id)
    employee_name = get_employee_name(employee_id)
    total_tasks = len(todos)
    done_tasks = sum(1 for task in todos if task.get("completed"))
    print(f"Employee {employee_name} is done with tasks"
          f"({done_tasks}/{total_tasks}):")
    for task in todos:
        if task.get("completed"):
            print(f"\t {task.get('title')}")


def get_employee_name(employee_id):
    """Retrieves the employee's name from the API"""
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    employee = response.json()
    return f"{employee.get('name')}"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            display_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer")
