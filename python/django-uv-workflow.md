# Django and UV workflow

Create a project folder

```
mkdir django-uv-test
```

Update uv:

```
uv self update

```

Start uv project:

```
uv init django-project --python 3.11

```

Add packages:

```
cd django-project
uv add Django django-extensions
```


Start Django project:

```
uv run django-admin startproject myproject .
```


Run Django management commands:

```
uv run manage.py runserver
uv run manage.py startapp appname
uv run manage.py makemigrations
uv run manage.py migrate
uv run manage.py shell_plus  # from django-extensions
```


Working with development dependencies:

```
uv add --dev black
uv run black path\to\file.py
```


Deploying the project to production excluding dev dependencies:

```
uv sync --no-dev
```


References

- [https://www.youtube.com/watch?v=hm-rDxSMzSw](https://www.youtube.com/watch?v=hm-rDxSMzSw)
