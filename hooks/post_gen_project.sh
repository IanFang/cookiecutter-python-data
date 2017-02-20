#!/bin/bash
git init
git add .
git commit -m "init commit"
git remote add origin {{ cookiecutter.git_url}}
