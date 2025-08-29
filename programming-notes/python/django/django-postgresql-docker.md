# Django and PostgreSQL setup in Docker

Here is how to dockerize a Django app along side a PostgreSQL database container.

This guide shows how to integrate the following tools:

- Docker containers
- uv package manager
- Django app
- PostgreSQL database


## Setup project

Project folder structure:

```bash
test-django-docker
├── .venv
├── my_django_app
│   ├── my_django_app
│   ├── core
│   └── manage.py
├── pyproject.toml
├── readme.md
├── requirements.txt
└── uv.lock
```

To set this up we create a root folder:

```bash
mkdir test-django-docker
cd test-django-docker
```

Since we are using `uv` to manage packages and environments we initiate it:

```bash
uv init .
```

Now lets create the Django project `my_django_app` and create the app `core`.

```bash
uv run django-admin startproject my_django_app
cd my_django_app
uv run python manage.py startapp core
```

On the root folder create a `requirements.txt` file:

```bash
cd ..
uv pip freeze > requirements.txt
```


## Adding `gunicorn`

Django `manage.py runserver` is only meant for development purposes and should be changed for a WSGI server for production.

```bash
uv add gunicorn
uv add "psycopg[binary]"
uv pip freeze > requirements.txt
```


## Create a Dockerfile

A Dockerfile is a script that tells Docker how to build your Docker image. Put it in the root directory of your Django project. Here’s a basic Dockerfile setup for Django:

```dockerfile
# Use the official Python runtime image
FROM python:3.11.13-slim-bookworm
 
# Create the app directory
RUN mkdir /app
 
# Set the working directory inside the container
WORKDIR /app
 
# Set several environment variables:
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1

# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1 
 
# Upgrade pip
RUN pip install --upgrade pip 
 
# Copy the Django project and install dependencies
COPY requirements.txt  /app/
 
# Install all dependencies 
RUN pip install --no-cache-dir -r requirements.txt
 
# Copy the Django project to the container
COPY . /app/
 
# Expose the Django port
EXPOSE 8000
 
# Run Django development server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Start the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "my_django_app.wsgi:application"]
```

Build the Docker container:

```bash
docker build -t django-docker .
```

To see your image, you can run:

```bash
docker image list
```


## Configure the Docker Compose file

A `docker-compose.yml` file allows you to manage multi-container applications. Here, we'll define both a Django container and a PostgreSQL database container.

```yaml
services:
  web:
    build: .
    container_name: django_app
    ports:
      - "8000:8000"
    volumes:
      - ./my_django_app:/app
    depends_on:
      db:
        condition: service_healthy
        restart: true
    env_file:
      - .env
  db:
    image: postgres:17
    container_name: postgres_db
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    healthcheck:
        test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
        interval: 10s
        retries: 5
        start_period: 30s
        timeout: 10s
    ports:
      - "5432:5432"
    volumes:
      - postgres_db:/var/lib/postgresql/data
    env_file:
      - .env
volumes:
  postgres_db:
```

The compose file makes use of an environment file called `.env`, which will make it easy to keep the settings separate from the application code.

```
POSTGRES_DB=postgres_db
POSTGRES_USER=dbuser
POSTGRES_PASSWORD=dbpassword
POSTGRES_HOST=db
POSTGRES_PORT=5432
```


## Update Django settings and configuration files

Let's update the `setting.py` file by:

- Adding the `core` app. 

- Change some variables to enable them to be set using environment variables when the container is started. This allows you to change these settings depending on the environment you are working in.

- Configure the database settings to use PostgreSQL.

```python
import os

# ...

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
 
DEBUG = bool(os.environ.get("DEBUG", default=0))
 
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS","127.0.0.1").split(",")

# ... 

INSTALLED_APPS = [
    # ...
    'core',
]

# ... 

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': os.environ['POSTGRES_DB'],
         'USER': os.environ['POSTGRES_USER'],
         'PASSWORD': os.environ['POSTGRES_PASSWORD'],
         'HOST': os.environ['POSTGRES_HOST'],
         'PORT': os.environ['POSTGRES_PORT'],
     }
 }
```





## References

- [Docker - Django and PostgreSQL setup (with uv) from scratch!](https://www.youtube.com/watch?v=37aNpE-9dD4)

- [How to Dockerize a Django App: Step-by-Step Guide for Beginners](https://www.docker.com/blog/how-to-dockerize-django-app/)

- [Dockerizing Django with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)