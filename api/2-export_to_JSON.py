#!/usr/bin/python3
"""Retrieves and exports an employee's TODO list progress in JSON format"""
import json
import requests
import sys


def get_employee_todos(employee_id):
    """Retrieves the employee's todos from the API"""
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    todos = response.json()
    return todos


def get_employee_name(employee_id):
    """Retrieves the employee's name from the API"""
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    employee = response.json()
    return f"{employee.get('name')}"


def export_todo_progress(employee_id):
    """Exports the employee's TODO list progress in JSON format"""
    todos = get_employee_todos(employee_id)
    employee_name = get_employee_name(employee_id)
    todo_data = []

    for task in todos:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee_name
        }
        todo_data.append(task_dict)

    filename = f"{employee_id}.json"
    todo_json = {str(employee_id): todo_data}

    with open(filename, mode='w') as jsonfile:
        json.dump(todo_json, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            export_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer")