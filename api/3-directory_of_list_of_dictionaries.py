#!/usr/bin/python3
"""Retrieves and exports all employees' TODO lists in JSON format"""
import json
import requests


def get_todos_by_user(user_id):
    """Retrieves the TODO list for a given user ID"""
    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    response = requests.get(url)
    todos = response.json()
    return todos


def get_username(user_id):
    """Retrieves the username for a given user ID"""
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    user = response.json()
    return user.get("username")


def export_todo_data():
    """Exports all employees' TODO lists in JSON format"""
    todo_data = {}

    for user_id in range(1, 11):  # Assuming user IDs range from 1 to 10
        todos = get_todos_by_user(user_id)
        username = get_username(user_id)

        user_todos = []
        for task in todos:
            task_dict = {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            user_todos.append(task_dict)

        todo_data[str(user_id)] = user_todos

    with open("todo_all_employees.json", mode='w') as jsonfile:
        json.dump(todo_data, jsonfile)


if __name__ == "__main__":
    export_todo_data()
