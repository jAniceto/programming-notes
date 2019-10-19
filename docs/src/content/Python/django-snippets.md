Title: Collection of useful Django snippets for several purposes
Date: 2019-01-08 10:32
Authors: José Aniceto
Modified: 2019-01-22 22:48

### Index
* [Create a slug](#create-a-slug)
* [Send email](#send-email)
* [Database dump to file](#database-dump-to-file)
* [Provide data to DB via Django Python Shell](#provide-data-to-db-via-django-python-shell)
* [Create script with access to Django shell](#create-script-with-access-to-django-shell)
* [Migrate Django from SQLite to PostgreSQL](#migrate-django-from-sqlite-to-postgresql)

---

### Create a slug
Call the Django `slugify` function automatically by overriding the `save` method. It is preferable to generate the slug only once when you create a new object, otherwise your URLs may change when the `q` field is edited, which can cause broken links. More info [here](https://stackoverflow.com/questions/837828/how-do-i-create-a-slug-in-django).

```python
# models.py

from django.utils.text import slugify

class Test(models.Model):
    q = models.CharField(max_length=30)
    s = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.s = slugify(self.q)

        super(Test, self).save(*args, **kwargs)
```

---

### Send email
If `html_message` keyword argument is provided, the resulting email will be a multipart/alternative email with `message` as the text/plain content type and `html_message` as the text/html content type. 

```python
# views.py

from django.core.mail import send_mail

send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)
```

Mail is sent using the SMTP host and port specified in the `EMAIL_HOST` and `EMAIL_PORT` settings. The `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` settings, if set, are used to authenticate to the SMTP server, and the `EMAIL_USE_TLS` and `EMAIL_USE_SSL` settings control whether a secure connection is used. More info [here](https://docs.djangoproject.com/en/2.1/topics/email/).

---

### Database dump to file
Save from DB
```
$ python manage.py dumpdata > db_dump.json
```

Load fixture to DB
```
$ python manage.py loaddata <fixture>
```

---

### Provide data to DB via Django Python Shell
Exemple for loading data in a json file named `filename.json` to the Model `Member` in the app `website`

```
$ python manage.py shell
```

```python
>>> import json
>>> from website.models import Member
>>> with open('filename.json', encoding="utf-8") as f:
...     members_json = json.load(f)
...
>>> for member in members_json:
...     member = Member(name=member['name'], position=member['position'], alumni=member['alumni'])
...     member.save()
...
>>> exit()
```

---

### Create script with access to Django shell
If you wnat to run an external script but have access to the Django environment like you do with `python manage.py shell` you can do the following. More info [here](https://stackoverflow.com/questions/8047204/django-script-to-access-model-objects-without-using-manage-py-shell)

```python
# your_script.py

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")

# your imports, e.g. Django models
from your_project_name.models import Location

# From now onwards start your script..
```

Here is an example to access and modify your model:
```python
# models.py

class Location(models.Model):
    name = models.CharField(max_length=100)
```

```python
# your_script.py

if __name__ == '__main__':    
    # e.g. add a new location
    l = Location()
    l.name = 'Berlin'
    l.save()

    # this is an example to access your model
    locations = Location.objects.all()
    print locations

    # e.g. delete the location
    berlin = Location.objects.filter(name='Berlin')
    print berlin
    berlin.delete()
```
---

### Migrate Django from SQLite to PostgreSQL

Here's how to migrate a Django database from SQLite to PostgreSQL. More info [here](https://stackoverflow.com/questions/3034910/whats-the-best-way-to-migrate-a-django-db-from-sqlite-to-mysql).

1) Dump existing data:
```
python manage.py dumpdata > datadump.json
```

2) Change settings.py to Postgres backend.

3) Make sure you can connect on PostgreSQL. Then:
```
python manage.py migrate --run-syncdb
```

4) Run this on Django shell to exclude contentype data
```
python manage.py shell
```
```
>>> from django.contrib.contenttypes.models import ContentType
>>> ContentType.objects.all().delete()
>>> quit()
````

5) Finally:
```
python manage.py loaddata datadump.json
```
