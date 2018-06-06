#!/usr/bin/env python3

import todoist
from sys import argv
from os import environ as env

user = env['USER']
with open(f'/home/{user}/.todoist', 'r') as file:
    token = str(file.readline().rstrip())

api = todoist.TodoistAPI(token)

args = argv[1:]

api.quick.add(' '.join(args))
api.commit()
