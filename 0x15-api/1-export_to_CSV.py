#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    completed_tasks = []
    for task in todos:
        completed_tasks.append([
            user_id,
            user.get("username"),
            task.get("completed"),
            task.get("title")
        ])

    csv_filename = "{}.csv".format(user_id)
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(
                csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        csv_writer.writerows(completed_tasks)
