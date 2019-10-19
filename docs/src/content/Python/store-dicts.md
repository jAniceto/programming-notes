Title: Storing dictionaries for later use: JSON and Pickle
Date: 2017-08-09 16:31
Authors: José Aniceto
Modified: 2017-08-12 15:07

## JSON

**Saving:**
```python
import json
with open('data.json', 'w') as fp:
    json.dump(data, fp)
```

Supply extra arguments like sort_keys or indent to get a pretty result. The argument sort_keys will sort the keys alphabetically and indent will indent your data structure with indent=N spaces.
```python
json.dump(data, fp, sort_keys=True, indent=4)
```

**Loading:**
```python
with open('data.json', 'r') as fp:
    data = json.load(fp)
```

#### json.dump() vs json.dumps(), json.load() vs json.loads()

If you want to dump the JSON into a file/socket or whatever, then you should go for `dump()`. If you only need it as a string (for printing, parsing or whatever) then use `dumps()` (dump string). The functions with an `s` take string parameters. The others take file streams.

---

## Pickle

**Saving:**
```python
import cPickle as pickle
with open('data.p', 'wb') as fp:
    pickle.dump(data, fp)
```

**Loading:**
```python
with open('data.p', 'rb') as fp:
    data = pickle.load(fp)
```
