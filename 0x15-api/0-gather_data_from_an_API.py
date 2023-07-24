#!/usr/bin/python3
"""This script returns to-do list information for a given employee ID."""
import requests
from sys import argv

if __name__ == "__main__":
    id = int(argv[1])

    url = "https://jsonplaceholder.typicode.com/todos"
    url2 = "https://jsonplaceholder.typicode.com/users"

    connect = requests.get(url).json()
    user = requests.get(url2).json()

    lst = []
    count = 0
    for done in connect:
        if done['userId'] == id and done['completed'] is True:
            lst.append(done['title'])
            count += 1
    task = 0
    for x in connect:
        if x['userId'] == id:
            task += 1

    for name in user:
        if name['id'] == id:
            print("Employee {} is done with tasks ({}/{})"
                  .format(name['name'], count, task))

    for x in lst:
        print("\t{}".format(x))

# Coded by EnGentech
