#!/usr/bin/python3
import requests
import sys


def tasks_done(id):
    """
        Script that returns info about empolyee todo list
    """

    base_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    response = requests.get(base_url)
    response_json = response.json()
    employee_name = response_json.get("name")

    base_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    todos = requests.get(base_url)
    todos_json = todos.json()
    number_tasks = len(todos_json)

    task_compleated = 0
    task_list = ""

    for task in todos_json:
        if task.get("completed") is True:
            task_compleated += 1
            task_list += "\t " + task.get("title") + "\n"

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          task_compleated,
                                                          number_tasks))
    print(task_list[:-1])


if __name__ == "__main__":
    tasks_done(sys.argv[1])