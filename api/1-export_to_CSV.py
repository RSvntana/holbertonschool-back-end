#!/usr/bin/python3
"""Retrieves and exports an employee's TODO list progress in CSV format"""
import csv
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
    """Exports the employee's TODO list progress in CSV format"""
    todos = get_employee_todos(employee_id)
    employee_name = get_employee_name(employee_id)
    filename = f"{employee_id}.csv"

    with open(filename, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            row = [
                employee_id,
                employee_name,
                task.get("completed"),
                task.get("title")
            ]
            csv_writer.writerow(row)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            export_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer")
