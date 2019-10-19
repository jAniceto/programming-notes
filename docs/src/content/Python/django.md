Title: Building a Django site
Date: 2018-04-03 17:23
Authors: José Aniceto
Modified: 2018-07-09 17:48

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

## Django authentication system

Base project struture for this section:

```
mysite/
  manage.py
  
  mysite/
    __init__.py
    settings.py
    urls.py
    wsgi.py
  
  app1/
    __init__.py
    admin.py
    apps.py
    migrations/
    models.py
    tests.py
    views.py
```

```python
# mysite/urls.py

```

```python
# mysite/urls.py

urlpatterns = [
  ...
  path('accounts/', include(django.contrib.auth.urls))
]
```

## Performing AJAX POST Requests in Django

Ref: http://coreymaynard.com/blog/performing-ajax-post-requests-in-django/

A common pitfall that shows up when developing a Django application is when you try and make your first POST request to your server from AJAX. As a response you receive a helpful 403 FORBIDDEN notice, and not much other information. There's a fairly simple way of handling this issue in a seamless fashion,.

Firstly, let's discuss the actual problem that is causing this. Django comes with a security feature called Cross Site Request Forgery protection. A CSRF attack is when some external malicious site contains a link with some JavaScript that is intended to perform an action on your web site using the credentials of a logged-in-user who visited the malicious site in their browser. To protect against this, Django adds a CSRF token to every request that must be included with every unsafe HTTP request method (POST, PUT, and DELETE). This random string is verified upon every request, and if it is not valid (or not present) the server will respond with 403 FORBIDDEN.

So, assuming you already have a Django project all setup and ready to go, we're going to create a view and a template to show the POST request in action. Just to keep things simple, we're going to do this in a separate app, so go ahead and create a new app and add it to your INSTALLED_APPS list. Inside of that app let's modify the views file and make it look like this:

```python
from django.views.generic import TemplateView
from django.http import HttpResponse

import json

class PostExample(TemplateView):
    template_name = 'start.html'

    def post(self, request):
        return HttpResponse(json.dumps({'key': 'value'}), mimetype="application/json")
```

What we're doing here is creating an incredibly basic view that on a GET request will respond with the `start.html` template and on a post request will respond with a hard coded JSON dictionary. Now we need to add the URL for this view to the project:

```python
url(r'^$', PostExample.as_view(), name='test-start'),
```

The template we're going to develop here will be equally simple, let's start with the following:

```html
<!DOCTYPE html>
<html>
<head>
<script src="{{ STATIC_URL }}js/jquery-1.11.1.min.js"></script>
<script type="text/javascript">
$(document).ready(function() {
    $("#post").click(function(e) {
        e.preventDefault();
        var data = {
            'foo': 'bar'
        }

        $.ajax({
            "type": "POST",
            "dataType": "json",
            "url": "/test/",
            "data": data,
            "success": function(result) {
                console.log(result);
            },
        });
    });
});
</script>
</head>
<body>
    <h1>PostExample</h1>
    <p><a href="" id="post">Post Request</a></p>
</body>
</html>
```

If you were to go to that page and click the link, you instead of a lovely JSON response you would see the 403 FORBIDDEN notice. Let's take care of that. The way to solve this is by overriding the jQuery beforeSend method on an AJAX query and grabbing the CSRF token embedded in the request and including it in the POST headers. Create a new JavaScript file and add the following to it, and make sure to include it into your template:

```javascript
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});
```

With that being done, all you have to do is add the CSRF token into the template like this:

```
{% raw %}{% csrf_token %}{% endraw %}
```

That takes care of it! You can now make AJAX POST requests from within your application, without doing any specific work on a per instance basis.

