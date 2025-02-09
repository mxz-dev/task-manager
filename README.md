# My Django To-Do App

Welcome to **Django To-Do App**! This is a [Django](https://www.djangoproject.com/) application built using class-based views (CBVs) and `django-allauth` for authentication.

## Features
- User authentication with `django-allauth`
- Create, update, delete, and view tasks
- Mark tasks as completed
- Responsive user-friendly interface (Tailwind CSS)

## Prerequisites
Before getting started, make sure you have the following installed on your system:
- [Docker](https://www.docker.com/) (with Docker Compose)
- Git

## Quick Start

Follow these steps to run the project on your local machine:

### 1. Clone the Repository and Run with Docker Compose (Recommended)
```bash
git clone https://github.com/mxz-dev/task-manager.git
cd task-manager
docker-compose up --build
```

### 2. Run & Install Manually (Optional)
```bash
cd task-manager
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```


# Todo
- [ ] Auth
  - [X] signup users
  - [X] login users
  - [X] logout users
  - [X] config profile
  - [X] confirm email
  - [ ] 2fa authenetication
- [X] Task
  - [X] add tasks
  - [X] change tasks
  - [X] delete tasks
  - [X] read tasks
  - [X] completed tasks
  - [X] paginated tasks
