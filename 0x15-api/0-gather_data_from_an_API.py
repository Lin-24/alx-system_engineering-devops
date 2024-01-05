#!/usr/bin/python3
"""Retrieves employee's TODO list progress from an API"""

from sys import argv
from json import load
import requests


if __name__ == "__main__":

    def make_request(resource, param=None):
        url = 'https://jsonplaceholder.typicode.com/'
        url += resource
        if param:
            url += ('?' + param[0] + '=' + param[1])

        r = requests.get(url)
        r = r.json()
        return r

    user = make_request('users', ('id', argv[1]))
    tasks = make_request('todos', ('userId', argv[1]))
    tasks_completed = [task for task in tasks if task['completed']]

    print('Employee {} is done with tasks({}/{}):'.format(user[0]['name'],
                                                          len(tasks_completed),
                                                          len(tasks)))
    for task in tasks_completed:
        print('\t {}'.format(task['title']))
