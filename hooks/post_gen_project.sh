#!/bin/bash
git init
git checkout -b master
git add .
git commit -m "init commit"
git checkout -b dev
git remote add origin {{ cookiecutter.git_url }}
