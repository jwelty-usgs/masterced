#!/bin/bash

environment=$1

cd /c/Users/sgce/source/sgce
git checkout $environment
git pull

rsync -avz --no-g --delete-after . /c/users/sgce/ced --exclude=support --exclude=README.md --exclude=.git --exclude=.gitignore --exclude=AlterForProduction.txt --exclude=requirements.txt

cd /c/Users/sgce/source/sgceconfig
git checkout $environment
git pull

rsync -avz --no-g --delete-after . /c/users/sgce/ced/config --exclude=.git --exclude=.gitignore

cd /c/Users/sgce/ced

ls
python -m compileall .
python manage.py check
date
