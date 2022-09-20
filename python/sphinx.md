# Sphinx

## Creating module pages automatically

```rst
Joback Method
=============

.. automodule:: chem_eng_kit.properties.joback
    :members:
    :exclude-members: _sum_group_property
```

## Creating docstrings

### Code blocks

```python
def foo():
    '''
    .. highlight:: python
    .. code-block:: python

        res = aFunction(something, goes, in)
        print(res.avalue)
    '''
```

Inline code in reStructuredText:

```python
def foo():
    '''
    bla `foo()` bla
    '''
```

Inline code in Markdown:

```python
def foo():
    '''
    bla ``foo()`` bla
    '''
```

### Math 

Displayed math:

```python
def foo():
    '''
    .. math:: V_c [cm^3/mol] = 17.5 + \\sum V_{c,i}
    '''
```

Inline math:

```python
def foo():
    '''
    where :math:`N_{atom}` is the number of atoms
    '''
```
