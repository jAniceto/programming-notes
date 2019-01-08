# Collection of useful Django snippets for several purposes

### Index
* [Create a slug](#create-a-slug)

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
