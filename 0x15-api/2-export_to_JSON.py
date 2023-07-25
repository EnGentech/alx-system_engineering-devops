#!/usr/bin/python3
"""Get API values and save into a json format"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    url2 = "https://jsonplaceholder.typicode.com/users"

    id = int(argv[1])

    todos = requests.get(url).json()
    users = requests.get(url2).json()

    my_list = []

    name = ""
    for get in users:
        if get['id'] == id:
            name = get['username']

    for todo in todos:
        if todo['userId'] == id:
            temp_list = {'task': todo['title'],
                         'completed': todo['completed'],
                         'username': name}
            my_list.append(temp_list)

    for user in users:
        if user['id'] == id:
            name = user['username']

    my_dictionary = {id: my_list}

    with open('{}.json'.format(id), 'w', encoding='utf') as file:
        json.dump(my_dictionary, file)

# Coded by EnGentech
