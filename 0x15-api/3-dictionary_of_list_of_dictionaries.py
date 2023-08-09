#!/usr/bin/python3
"""Exports to-do list information for all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()

    user_data = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        user_data[user_id] = []
        for task in todos:
            if task.get("userId") == user_id:
                user_data[user_id].append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })

    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w') as json_file:
        json.dump(user_data, json_file)
