# Collection of useful Django snippets for several purposes

### Index
* [Create a slug](#create-a-slug)
* [Send email](#send-email)
* [Database dump to file](#database-dump-to-file)
* [Provide data to DB via Django Python Shell](#provide-data-to-db-via-django-python-shell)

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
