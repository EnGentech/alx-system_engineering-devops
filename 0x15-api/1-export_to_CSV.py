#!/usr/bin/python3
"""Get API values and save into a csv format"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    url2 = "https://jsonplaceholder.typicode.com/users"

    id = int(argv[1])

    todos = requests.get(url).json()
    users = requests.get(url2).json()

    name = ""
    for user in users:
        if user['id'] == id:
            name = user['username']

        with open("{}.csv".format(id), "w", newline="") as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for todo in todos:
                if todo['userId'] == id:
                    writer.writerow(
                        [id, name, todo.get("completed"), todo.get("title")])

# Coded by EnGentech
