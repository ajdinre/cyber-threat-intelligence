#!/bin/sh

cd client
ng build --watch &
cd ../django_project
python3 manage.py runserver
