# Building a Django site

## Installing Django

`pip install Django`

## Start project

Navigate via the terminal or command prompt to an area where you want to work on your project, then do:

`django-admin startproject mysite`

This will create a directory called mysite. Within that directory, you have another one called mysite, along with a manage.py file. The manage.py file lets you easily interact with your project via the command line. The contents of the second mysite directory contain your settings and urls mainly. Broken down:

```cmd
/mysite/  REM Simple container, Call whatever you want.
    manage.py  REM Lets you interact with your project via the command line.
    /mysite/  REM Actual project directory.
        __init__.py  REM Tells python this is a Python package.
        settings.py  REM Settings for the project.
        urls.py  REM URL rules. Django docs aptly describes as your table of contents.
        wsgi.py  REM WSGI magic begins here. Worry about this when it comes time to actually deploy to a server.
```

The paradigm of Django is that either a website is an app, or a collection of apps in most cases. We currently have our website, called "mysite" for now. For now, run the following via the command line or terminal to run the local development server, which you can reach at http://127.0.0.1:8000. 

```
cd mysite
python manage.py runserver
```

### Create an app

`python manage.py startapp webapp`

Now a new directory exists, called webapp. In here, we see a lot of similar files, and some new ones:

```
webapp/
    migrations/ 
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
```

Next, we need to include our new app in our installed applications:

Open the `mysite/settings.py` file and add the `'webapp'` line:

```python
# ...this is just a slice of code within settings.py 
# do not delete the other code
# just add 'webapp' to the list.
INSTALLED_APPS = [
    'webapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

### Make migrations (databases)

Whenever you define new models, you need to migrate: 

`python manage.py makemigrations`

The `makemigrations` command tells Django that you've made some model changes, and you want to save them as a migration. Migrations are used any time you want Django to recognize changes to the models and database schema. **Adding data to an existing database table, for example, is not something that needs a migration, changing that table's structure (by changing the model), would require a migration.** You can also tell Django you want to make migrations for only a specific app, like: `python manage.py makemigrations webapp`

Once you've made migrations, nothing has actually happened yet. You can run a migrate, but there is one more check you can make. This will output the proposed SQL that will be run for you by Django when you migrate. The `0001` is the migration ID. You can see this on the `0001_initial.py` file in the migrations folder of your app.

`python manage.py sqlmigrate webapp 0001` (Optional)

If all looks good, you can run the `migrate` command. This will actually perform the migrations. If this is your first time doing this, you should see quite a bit has been migrated.

`python manage.py migrate`


### Admin control panel

To access the admin page, you visit /admin/, assuming the admin app is indeed installed. To login to the admin panel you need to create an user:

`python manage.py createsuperuser`

To register a model create a webapp/admin.py file, and in it put:

```python
from django.contrib import admin
from webapp.models import Post

admin.site.register(Post)
```

Here, we are importing the admin, the Post model, and then we're registering the Post model.


## Using MySQL database 

By default Django works with SQLite database management system. First, create the MySQL database using the MySQL shell: 

`CREATE DATABASE django_db;`

To use MySQL in Django, instead of SQLite, do the following:

`pip install mysqlclient`

Go to the main `settings.py` file and modify the DATABASES section to:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_db',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': ''
    }
}
```
Now you can run the migrate command to create all tables Django needs: `python manage.py migrate`
