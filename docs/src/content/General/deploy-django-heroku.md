Title: Deploy a Django app to Heroku
Date: 2019-01-22 14:45
Authors: José Aniceto
Modified: 2019-02-01 23:11

### Index:
* [Requirements](#requirements)
* [Install the Heroku CLI](#install-the-heroku-cli)
* [Deploying Python and Django Apps on Heroku](#deploying-python-and-django-apps-on-heroku)
* [Configure Django apps for Heroku](#configure-django-apps-for-heroku)
* [Deploy to Heroku](#deploy-to-heroku)
* [References](#references)


### Requirements:
* Git installed
* Python >3.6
* Heroku CLI (see step 1)


## 1) Install the Heroku CLI

Install the Heroku Command Line Interface (CLI) for your platform from [here](https://devcenter.heroku.com/articles/getting-started-with-python#set-up). Once installed, you can use the `heroku` command from your command shell. To log in to the Heroku CLI use:

```bash
$ heroku login
```


## 2) Deploying Python and Django apps on Heroku

Heroku automatically identifies your app as a Python app if any of the following files are present in its root directory:
* `Pipfile`
* `setup.py`
* `requirements.txt`

When you deploy to Heroku, the dependencies you specify are automatically installed. If you’re using Django, the `collectstatic` command also runs automatically during the deployment process. For this to work properly make sure you install the Django-Heroku Python package (step 3).


## 3) Configure Django apps for Heroku

Create a `Procfile` (no extension) and add the following content where `myproject` is the name of your Django app.
```
web: gunicorn myproject.wsgi
```

Install `gunicorn`:
```bash
$ pipenv install gunicorn
```

Install the `django-heroku` package
```bash
$ pipenv install django-heroku
```

Add the following import statement to the top of `settings.py`:
```python
import django_heroku
```
Then add the following to the bottom of `settings.py`:
```python
# Activate Django-Heroku.
django_heroku.settings(locals())
```


## 4) Deploy to Heroku

Using the Heroku CLI lets create our app and the database.

```bash
$ heroku login
$ heroku create <desired_app_name>
```

Now lets push our code to Heroku:
```bash
$ git add .
$ git commit -m "Ready to heroku this."
$ git push heroku master
```

Finally, migrate your Database to the Heroku app:

```bash
$ heroku run python manage.py migrate
```

You should now be able to see your app in the Heroku Dashboard as well as a Dyno web process with the `ON` indication.


## 5) Import local database to Heroku (Optional)

If you are using a postgresql database locally you can easily import it to your newly created Heroku app. First create a backup of your local DB:

```bash
pg_dump -U USERNAME DATABASE > pg_db_dump.sql
```

To import it to Heroku run:

```bash
heroku pg:psql --app APPNAME < pg_db_dump.sql
```

### References:
* [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python)
* [Deploying Python and Django Apps on Heroku](https://devcenter.heroku.com/articles/deploying-python)
* [Configuring Django Apps for Heroku](https://devcenter.heroku.com/articles/django-app-configuration)
* [django-heroku Github](https://github.com/heroku/django-heroku)
* [Deploying with Git](https://devcenter.heroku.com/articles/git)
