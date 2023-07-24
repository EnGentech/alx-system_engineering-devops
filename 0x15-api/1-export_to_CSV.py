#!/usr/bin/python3
"""Get API values and save into a csv format"""

import requests
import csv
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    url2 = "https://jsonplaceholder.typicode.com/users"

    id = argv[1]

    todos = requests.get(url).json()
    users = requests.get(url2).json()

    name = ""
    for user in users:
        if user['id'] == id:
            name = user['username']

        with open("{}.csv".format(id), "w", newline="") as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            [writer.writerow(
                [id, name, t.get("completed"), t.get("title")]
            ) for t in todos]

    # with open("{}.csv".format(id), 'w') as f:
    #     writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    #     for todo in todos:
    #         if todo['userId'] == id:
    #             val = [id, name, todo["completed"], todo["title"]]
    #             writer.writerow([val])

# Coded by EnGentech
