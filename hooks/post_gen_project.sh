#!/bin/bash
git init
git checkout -b dev
git checkout -b master
git add .
git commit -m "init commit"
git remote add origin {{ cookiecutter.git_url }}
