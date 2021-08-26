# Configuration files

Most interesting programs need some kind of configuration. For very simple tasks you might choose to write these configuration variables directly into the source code. But this is a bad idea when you want to distribute your code and allow users to change configurations. Here are a few alternatives on how to handle configuration files in Python.

## Using a `.ini` file [*](https://wiki.python.org/moin/ConfigParserExamples)

Create a `myfile.ini` like:
```ini
[SectionOne]
Status: Single
Name: Derek
Value: Yes
Age: 30
Single: True

[SectionTwo]
FavoriteColor=Green
[SectionThree]
FamilyName: Johnson

[Others]
barList=item1,item2
```

Retrieve the data like:
```python
>>> import ConfigParser
>>> Config = ConfigParser.ConfigParser()
>>> Config
<ConfigParser.ConfigParser instance at 0x00BA9B20>
>>> Config.read("myfile.ini")
['c:\\tomorrow.ini']
>>> Config.sections()
['Others', 'SectionThree', 'SectionOne', 'SectionTwo']
>>> Config.options('SectionOne')
['Status', 'Name', 'Value', 'Age', 'Single']
>>> Config.get('SectionOne', 'Status')
'Single'
```

## Using YAML [*](https://camel.readthedocs.io/en/latest/yamlref.html)
YAML is a human friendly data serialization standard for all programming languages.

Create a `config.yml` file
```yaml
database:
    username: admin
    password: foobar  # TODO get prod passwords out of config
    socket: /var/tmp/database.sock
    options: {use_utf8: true}
memcached:
    host: 10.0.0.99
workers:
  - host: 10.0.0.101
    port: 2301
  - host: 10.0.0.102
    port: 2302
```

Parse with:
```python
import yaml
config = yaml.safe_load(open("config.yml"))
```

## Using a Python module

Create a regular Python module, say `config.py`, like this:
```python
truck = dict(
    color = 'blue',
    brand = 'ford',
)
city = 'new york'
cabriolet = dict(
    color = 'black',
    engine = dict(
        cylinders = 8,
        placement = 'mid',
    ),
    doors = 2,
)
```

Use it like this:
```python
import config
print(config.truck['color'])  
```

## Other alternatives
- Using a JSON file


## References
- [What's the best practice using a settings file in Python?](https://stackoverflow.com/questions/5055042/whats-the-best-practice-using-a-settings-file-in-python/34354110#34354110)
- [Configuration files in Python](https://martin-thoma.com/configuration-files-in-python/)
