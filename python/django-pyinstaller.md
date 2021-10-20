# Create a executable Django App

Since PyInstaller 2.1, you can build an executable from a project using Django 2.1.8. PyInstaller will take care of a _lot_ of the magic needed to correctly build Django applications. For instance, it will parse all your files and find all the dotted-names strings that refer to module names (eg: within `settings.py`) and make sure that all those modules are packaged.

You should be able to run PyInstaller over the `manage.py` script directly.

The following example should clarify the required steps.

## Example

Let's say that your Django project is called `mysite`. If you used the `django-admin.py` wizard, you probably have ended up with a [Django project directory structure](https://docs.djangoproject.com/en/1.8/intro/tutorial01/). PyInstaller expects a directory structure like this:
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
        ...
```
Use PyInstaller:
```console
$ pyinstaller --name=mysite mysite/manage.py
```
Notice the use of the `--name` option to make sure the output is a packaged executable called `mysite` and not `manage` from the script name.

Now you should have a frozen django app in the directory `./dist/mysite/`. You should be able to see an executable file `./dist/mysite/mysite.exe`. Use this file the same way as you would use `manage.py`.

To run the built-in Django test server run:
```console
$ ./dist/mysite/mysite.exe runserver localhost:8000
```

## Multiple Settings Modules

If you're using multiple settings files in your Django project, you'll need to do a bit more work to get pyinstaller to use the correct one. Say you had the following configuration:

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings/
            __init__.py
            base.py
            development.py
            production.py
        urls.py
        wsgi.py
```

In this case, if you want PyInstaller to use `mysite.settings.production`, you should modify `mysite/settings/__init__.py` to include the following:

```python
from production import *
```

This is required because PyInstaller only looks for settings files at two locations: either `mysite/settings.py`, or `mysite/settings`.


## What if it does not work?

Django uses a lot of magic under the hood, so some quirks are expected. If the application does not run, you should see the traceback in the console. If it is an `ImportError`, it is probably a missing module whose dependency PyInstaller was not able to automatically discover.

The quickest workaround is to add an import statement for that module, for instance in the `manage.py` script. But please report the incident to the mailing list so that we can prepare a proper fix that everyone can benefit from.

If this does not help, have a look at [[How to Report Bugs#before-submitting-a-report-make-sure-everything-is-packaged]] to track down the problem.
