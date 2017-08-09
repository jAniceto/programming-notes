# Storing dictionaries for later use: JSON and Pickle

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
