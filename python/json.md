# Working with JSON

## Saving

```python
import json
with open('data.json', 'w') as fp:
    json.dump(data, fp)
```

Supply extra arguments like sort_keys or indent to get a pretty result. The argument sort_keys will sort the keys alphabetically and indent will indent your data structure with indent=N spaces.

```python
json.dump(data, fp, sort_keys=True, indent=4)
```

## Loading
```python
with open('data.json', 'r') as fp:
    data = json.load(fp)
```

#### json.dump() vs json.dumps(), json.load() vs json.loads()

If you want to dump the JSON into a file/socket or whatever, then you should go for `dump()`. If you only need it as a string (for printing, parsing or whatever) then use `dumps()` (dump string). The functions with an `s` take string parameters. The others take file streams.

## Query JSON
JMESPath is a query language for JSON, which allows you to obtain the data you need from a JSON document or dictionary easily. This library is available for Python, but also for many other programming languages, meaning that if you master the JMESPath query language, you can use it in many places. Here's some example code to get a feeling for what's possible:

```python
import jmespath

persons = {
   "persons": [
     { "name": "erik", "age": 38 },
     { "name": "john", "age": 45 },
     { "name": "rob", "age": 14 }
   ]
}
jmespath.search('persons[*].age', persons)
# [38, 45, 14]
```

## References
- [python.land/data-processing/working-with-json/jmespath](https://python.land/data-processing/working-with-json/jmespath)
