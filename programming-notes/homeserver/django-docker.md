# Django web-app in Docker container

<sub><sup>Reference: [Docker - Django and PostgrSQL setup (with uv) from scratch!](https://www.youtube.com/watch?v=37aNpE-9dD4)</sub></sup>

<sub><sup>Reference: [Using uv in Docker](https://docs.astral.sh/uv/guides/integration/docker/)</sub></sup>

This guide shows how to integrate the following tools:

- Docker containers
- uv package manager
- Django app
- PostgreSQL database


## Set up Django app

Create a project folder:

```bash
mkdir django-docker-demo
cd django-docker-demo
```

Create Django project and Django app:

```bash
django-admin startproject django-docker-demo .
python manage.py startapp core
```

We now have the following directory structure:

```
django-docker-demo
|-- django-docker-demo
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- core
|   |-- ...
|   |-- views.py
|   |-- ...
```

Don't forget to add the `core` app to the `INSTALLED_APPS` (in `settings.py`).

Now we need to add a `Dockerfile` in the project root folder

```
FROM python:3.13.3-slim-bookworm

ENVPYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y curl

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/ 

COPY src/requirements.txt .
RUN uv pip install -r requirements.txt --system

COPY src/ .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

New lets create a `docker-compose.yaml` file:

```
services:
  web:
    build: .
    container_name: django_app
    ports:
      - 8000:8000
    volumes:
      - ./django-docker-demo:app/
```

```bash
docker-compose up --build
```

## Add PostgreSQL database

Lets add this new service to the `docker-compose.yaml` file:

```
services:
  web:
    build: .
    container_name: django_app
    ports:
      - 8000:8000
    volumes:
      - ./django-docker-demo:app/
    depends_on:
      db:
        condition: service_healthy
        restart: true
    env_file:
      - .env
  db:
    image: postgres:17
    container_name: postgres_db
    volumes:
      - postgres_db:/var/lib/postgresql/data/
    environment:
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
    healthcheck:
      test: ["CMD_SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
      interval: 10s
      retires: 5
      start_period: 30s
volumes:
  postgres_db:
```

Lets create the `.env` file:

```
POSTGRES_DB=demo_db
POSTGRES_USER=username
POSTGRES_PASSWORD=test
DB_HOST=db
DB_PORT=5432
```

And lets change the Django `settings.py` file for the PostgreSQL database:

```
import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": os.environ["DB_HOST"],
        "PORT": os.environ["DB_PORT"],
    }
}
```

Finally, we can run the `docker-compose.yaml` file:

```bash
docker-compose up
```

## Executing commands

After something like creating models, you may want to run migrations:

```bash
docker exec django_app python manage.py makemigrations
docker exec django_app python manage.py migrate
```

And to access the PostgreSQL shell:

```bash
docker exec -ti django_app postgres_db psql -U username -d demo_db
```

or to access the Django shell:

```bash
docker exec -ti django_app manage.py shell
```


## Creating an entrypoint

You may want to create an entrypoint.

In the same level as the `manage.py` file create a `entrypoint.sh` file:

```
#!/bin/sh

echo "Running migrations..."
python manage.py migrate

echo "Starting server..."
python manage.py runserver 0.0.0.0:8000
```

Then:

```bash
chmod +x entrypoint.sh
```

You can now go to your `Dockerfile` and change the final line:

```
# ...

CMD ["./entrypoint.sh"]
```

```bash
docker-compose up
```