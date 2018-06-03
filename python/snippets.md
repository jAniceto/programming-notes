# Useful Python code snippets

A collection of several code snippets of common or useful operation in Python.

## Remove dictionary from list

Here's how to remove a specific dictionary, or several dictionaries, from a list of dictionaries by a specific key. In the example below we are removing from the list all dictionaries which have and `id` key of `2`.

```python
thelist = [{'id': 1, 'name': 'paul'},
           {'id': 2, 'name': 'john'}]
           
thelist[:] = [d for d in thelist if d.get('id') != 2]
```
