#!/usr/bin/python3
"""Get API values and save into a json format"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    url2 = "https://jsonplaceholder.typicode.com/users"

    todos = requests.get(url).json()
    users = requests.get(url2).json()

    my_dictionary = {}

    for x in range(1, len(users) + 1):
        id = x

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

        temp_dic = {id: my_list}
        my_dictionary.update(temp_dic)

    with open("todo_all_employees.json", 'w', encoding='utf') as file:
        json.dump(my_dictionary, file)

# Coded by EnGentech
