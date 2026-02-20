# TaskFlow API

TaskFlow is a Django REST API that allows users to manage tasks.

## Features

- User authentication (JWT)
- Create, update, delete tasks
- Mark tasks as complete/incomplete
- User-specific task access

## Tech Stack

- Django
- Django REST Framework
- Simple JWT
- SQLite (development)

## Setup

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
