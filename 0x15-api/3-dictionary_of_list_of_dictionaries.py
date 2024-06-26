#!/usr/bin/python3
import json
import requests
import sys


def tasks_done():
    """
        script to return employee todo list
    """

    id = 1
    all_todos = {}
    while True:
        base_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
        response = requests.get(base_url)
        response_json = response.json()
        if len(response_json) == 0:
            break
        employee_name = response_json.get("name")

        base_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
        todos = requests.get(base_url)
        todos_json = todos.json()
        task_list = []

        for task in todos_json:
            task_dict = {}
            task_dict["task"] = task.get("title")
            task_dict["completed"] = task.get("completed")
            task_dict["username"] = employee_name
            task_list.append(task_dict)

        all_todos[id] = task_list
        id += 1

    file_name = "todo_all_employees.json"
    with open(file_name, "a") as fd:
        json.dump(all_todos, fd)


if __name__ == "__main__":
    tasks_done()
