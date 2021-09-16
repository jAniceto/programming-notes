# Data structures
Python offers several data structures such as:
- Strings
- Lists
- Tuples
- Dictionaries
- Sets
- Deques

We'll cover some of these below.


## Tuples
Tuples are an ordered collection of values that cannot be modified at runtime. This module shows how tuples are created, iterated, accessed and combined.

This is a tuple of integers:
```python
immutable = (1, 2, 3, 4)
```

It can be indexed like a list:
```python
assert immutable[0] == 1
assert immutable[-1] == 4
```

It can be sliced like a list:
```python
assert immutable[1:3] == (2, 3)
assert immutable[3:4] == (4,)
assert immutable[1::2] == (2, 4)
assert immutable[::-1] == (4, 3, 2, 1)
```

It can be iterated over like a list:
```python
for ix, number in enumerate(immutable):
    assert immutable[ix] == number
```

But its contents cannot be changed. As an alternative, we can create new tuples from existing tuples 
```python
bigger_immutable = immutable + (5, 6)
assert bigger_immutable == (1, 2, 3, 4, 5, 6)
smaller_immutable = immutable[0:2]
assert smaller_immutable == (1, 2)
```

We use tuples when the number of items is consistent. An example where this can help is a 2D game with X and Y coordinates. Using a tuple with two numbers can ensure that the number of coordinates doesn't change to one, three, four, etc.
```python
moved_count = 0
pos_x, pos_y = (0, 0)
for i in range(1, 5, 2):
    moved_count += 1
    pos_x, pos_y = (pos_x + 10 * i, pos_y + 15 * i)
assert moved_count == 2
assert pos_x == 40 and pos_y == 60
```

## Sets
Sets are an unordered collection of unique values that can be modified at
runtime. This module shows how sets are created, iterated, accessed,
extended and shortened.

Let's define one `set` for starters:
```python
simple_set = {0, 1, 2}
```

A set is dynamic like a `list` and `tuple`:
```python
simple_set.add(3)
simple_set.remove(0)
assert simple_set == {1, 2, 3}
```

Unlike a `list` and `tuple`, it is not an ordered sequence as it does not allow duplicates to be added:
```python
for _ in range(5):
    simple_set.add(0)
    simple_set.add(4)
    assert simple_set == {0, 1, 2, 3, 4}
```

Now let's define two new `set` collections:
```python
multiples_two = set()
multiples_four = set()
```

Fill sensible values into the set using `add`:
```python
for i in range(10):
    multiples_two.add(i * 2)
    multiples_four.add(i * 4)
```

As we can see, both sets have similarities and differences:
```python
assert multiples_two == {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}
assert multiples_four == {0, 4, 8, 12, 16, 20, 24, 28, 32, 36}
```

We cannot decide in which order the numbers come out - so let's look for fundamental truths instead, such as divisibility against 2 and 4. We do this by checking whether the modulus of 2 and 4 yields 0 (i.e. no remainder from performing a division):
```python
multiples_common = multiples_two.intersection(multiples_four)
for number in multiples_common:
    assert number % 2 == 0 and number % 4 == 0
```

We can compute exclusive multiples:
```python
multiples_two_exclusive = multiples_two.difference(multiples_four)
multiples_four_exclusive = multiples_four.difference(multiples_two)
assert len(multiples_two_exclusive) > 0
assert len(multiples_four_exclusive) > 0
```

Numbers in this bracket are greater than 2 * 9 and less than 4 * 10:
```python
for number in multiples_four_exclusive:
    assert 18 < number < 40
```

By computing a set union against the two sets, we have all integers in this program:
```python
multiples_all = multiples_two.union(multiples_four)
```

Check if set A is a subset of set B:
```python
assert multiples_four_exclusive.issubset(multiples_four)
assert multiples_four.issubset(multiples_all)
```

Check if set A is a subset and superset of itself:
```python
assert multiples_all.issubset(multiples_all)
assert multiples_all.issuperset(multiples_all)
```

Check if set A is a superset of set B:
```python
assert multiples_all.issuperset(multiples_two)
assert multiples_two.issuperset(multiples_two_exclusive)
```


## References
- [Ultimate Python - Tuples](https://github.com/huangsam/ultimate-python/blob/master/ultimatepython/data_structures/tuple.py)
- [Ultimate Python - Sets](https://github.com/huangsam/ultimate-python/blob/master/ultimatepython/data_structures/set.py)
