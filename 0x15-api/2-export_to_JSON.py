#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    user_data = {user_id: []}
    for task in todos:
        user_data[user_id].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        })

    json_filename = "{}.json".format(user_id)
    with open(json_filename, mode='w') as json_file:
        json.dump(user_data, json_file)
