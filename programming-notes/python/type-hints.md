# Python type hints

Python has support for optional "type hints". These "type hints" are a special syntax that allow declaring the type of a variable. By declaring types for your variables, editors and tools can give you better support.

## Variables

This is how you declare the type of a variable type in Python 3.6+:

```python
age: int = 1
```

You don't need to initialize a variable to annotate it:

```python
a: int  # Ok (no value at runtime until assigned)
```

This is useful in conditional branches:

```python
child: bool
if age < 18:
    child = True
else:
    child = False
```

## Built-in types

```python
from typing import List, Set, Dict, Tuple, Optional
```

For simple built-in types, just use the name of the type:

```python
x: int = 1
x: float = 1.0
x: bool = True
x: str = "test"
x: bytes = b"test"
```

For collections, the type of the collection item is in brackets (Python 3.9+):

```python
x: list[int] = [1]
x: set[int] = {6, 7}
```

Note: In Python 3.8 and earlier, the name of the collection type is capitalized, and the type is imported from the `typing` module:

```python
x: List[int] = [1]
x: Set[int] = {6, 7}
```

For mappings, we need the types of both keys and values:

```python
x: dict[str, float] = {"field": 2.0}  # Python 3.9+
```

For tuples of fixed size, we specify the types of all the elements:

```python
x: tuple[int, str, float] = (3, "yes", 7.5)  # Python 3.9+
```

For tuples of variable size, we use one type and ellipsis:

```python
x: tuple[int, ...] = (1, 2, 3)  # Python 3.9+
```

Use `Optional[]` for values that could be `None`:

```python
x: Optional[str] = some_function()
```

## Functions

```python
from typing import Callable, Iterator, Union, Optional
```

This is how you annotate a function definition:

```python
def stringify(num: int) -> str:
    return str(num)
```

And here's how you specify multiple arguments:

```python
def plus(num1: int, num2: int) -> int:
    return num1 + num2
```

Add default value for an argument after the type annotation:

```python
def f(num1: int, my_float: float = 3.5) -> float:
    return num1 + my_float
```

This is how you annotate a callable (function) value:

```python
x: Callable[[int, float], float] = f
```

A generator function that yields ints is secretly just a function that returns an iterator of ints, so that's how we annotate it:

```python
def g(n: int) -> Iterator[int]:
    i = 0
    while i < n:
        yield i
        i += 1
```

You can of course split a function annotation over multiple lines:

```python
def send_email(address: Union[str, list[str]],
               sender: str,
               cc: Optional[list[str]],
               bcc: Optional[list[str]],
               subject='',
               body: Optional[list[str]] = None
               ) -> bool:
    ...
```

An argument can be declared positional-only by giving it a name starting with two underscores:

```python
def quux(__x: int) -> None:
    pass

quux(3)  # Fine
quux(__x=3)  # Error
```

## More advanced stuff

Use `Union` when something could be one of a few types:

```python
x: list[Union[int, str]] = [3, 5, "test", "fun"]
```

Use `Any` if you don't know the type of something or it's too dynamic to write a type for:

```python
x: Any = mystery_function()
```

This makes each positional argument and each keyword arg a `str`:

```python
def call(self, *args: str, **kwargs: str) -> str:
    request = make_request(*args, **kwargs)
    return self.do_api_query(request)
```

## Standard "duck types"

In typical Python code, many functions that can take a list or a dict as an argument only need their argument to be somehow "list-like" or "dict-like". A specific meaning of "list-like" or "dict-like" (or something-else-like) is called a "duck type", and several duck types that are common in idiomatic Python are standardized.

```python
from typing import Mapping, MutableMapping, Sequence, Iterable
```

Use `Iterable` for generic iterables (anything usable in `for`), and `Sequence` where a sequence (supporting `len` and `__getitem__`) is required:

```python
def f(ints: Iterable[int]) -> list[str]:
    return [str(x) for x in ints]

f(range(1, 3))
```

`Mapping` describes a dict-like object (with `__getitem__`) that we won't mutate, and `MutableMapping` one (with `__setitem__`) that we might:

```python
def f(my_mapping: Mapping[int, str]) -> list[int]:
    my_mapping[5] = 'maybe'  # if we try this, mypy will throw an error...
    return list(my_mapping.keys())

f({3: 'yes', 4: 'no'})
```

```python
def f(my_mapping: MutableMapping[int, str]) -> set[str]:
    my_mapping[5] = 'maybe'  # ...but mypy is OK with this.
    return set(my_mapping.values())

f({3: 'yes', 4: 'no'})
```

## Classes

```python
class MyClass:
    # You can optionally declare instance variables in the class body
    attr: int
    # This is an instance variable with a default value
    charge_percent: int = 100

    # The "__init__" method doesn't return anything, so it gets return type "None" just like any other method that doesn't return anything
    def __init__(self) -> None:
        ...

    # For instance methods, omit type for "self"
    def my_method(self, num: int, str1: str) -> str:
        return num * str1
```

User-defined classes are valid as types in annotations:

```python
x: MyClass = MyClass()
```

You can use the `ClassVar` annotation to declare a class variable:

```python
class Car:
    seats: ClassVar[int] = 4
    passengers: ClassVar[list[str]]
```

You can also declare the type of an attribute in `__init__`:

```python
class Box:
    def __init__(self) -> None:
        self.items: list[str] = []
```


## References

- [mypy - Type hints cheat sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)
- [FastAPI - Python Types Intro](https://fastapi.tiangolo.com/python-types/)
