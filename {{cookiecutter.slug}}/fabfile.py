"""
Automate frequently used tasks
"""

from fabric.api import *
import os
import os.path

work_path = os.path.dirname(os.path.realpath(__file__))


def push():
    with lcd(work_path):
        local('git checkout master')
        local('git push origin master')
        local('git checkout dev')
        local('git push origin dev')


def pull():
    with lcd(work_path):
        local('git checkout master')
        local('git pull origin master')
        local('git checkout dev')
        local('git pull origin dev')


def ckupd():
    with lcd(work_path):
        local('git fetch')
        local('gitk --all')


def clean():
    with lcd(work_path):
        local('rm -rf tests/*.pyc')
        local('sudo rm -rf tests/__pycache__')


def reindex():
    dirs = ['data/interim',
            'data/processed',
            'data/raw',
            'data/results']
    for dir in dirs:
        loc = os.path.join(work_path, dir)
        with lcd(loc):
            local('ls -1 -I index.txt > index.txt')