Title: Useful Python code snippets
Date: 2018-06-03 14:27
Authors: José Aniceto
Modified: 2018-06-06 13:49

A collection of several code snippets of common or useful operation in Python.

## Remove dictionary from list

Here's how to remove a specific dictionary, or several dictionaries, from a list of dictionaries by a specific key. In the example below we are removing from the list all dictionaries which have and `id` key of `2`.

```python
thelist = [{'id': 1, 'name': 'paul'},
           {'id': 2, 'name': 'john'}]
           
thelist[:] = [d for d in thelist if d.get('id') != 2]
```

## List Comprehension

Without list comprehension:

```python
x = [1,2,3,4]
out = []
for item in x:
    out.append(item**2)
print(out)
# [1, 4, 9, 16]
```

With list comprehension:

```python
x = [1,2,3,4]
out = [item**2 for item in x]
print(out)
# [1, 4, 9, 16]
```

## Lambda Functions

Lambda functions are used for creating small, one-time and anonymous function objects in Python. Basically, they let you create a function, without creating a function. Note that lambda functions can do everything that regular functions can do, as long as there’s just one expression. The basic syntax of lambda functions is: `lambda arguments: expression`. And here is an example:

```python
double = lambda x: x * 2
print(double(5))
# 10
```

## Map and Filter

Once you have a grasp on lambda functions, learning to pair them with the map and filter functions can be a powerful tool. Specifically, **map** takes in a list and transforms it into a new list by performing some sort of operation on each element. In this example, it goes through each element and maps the result of itself times 2 to a new list. Note that the list function simply converts the output to list type.

```python
seq = [1, 2, 3, 4, 5]
list(map(lambda var: var*2, seq))
 #[2, 4, 6, 8, 10]
```

The **filter** function takes in a list and a rule, much like map, however it returns a subset of the original list by comparing each element against the boolean filtering rule.

```python
seq = [1, 2, 3, 4, 5]
list(filter(lambda x: x > 2, seq))
# [3, 4, 5]
```

[![IMAGE ALT TEXT](http://img.youtube.com/vi/cKlnR-CB3tk/0.jpg)](http://www.youtube.com/watch?v=cKlnR-CB3tk "Python: Lambda, Map, Filter, Reduce Functions")

## Arange and Linspace

For creating quick and easy Numpy arrays, look no further than the arange and linspace functions. Each one has their specific purpose, but the appeal here (instead of using range), is that they output NumPy arrays, which are typically easier to work with for data science.

**Arange** returns evenly spaced values within a given interval. Along with a starting and stopping point, you can also define a step size or data type if necessary. Note that the stopping point is a ‘cut-off’ value, so it will not be included in the array output.

```python
# np.arange(start, stop, step)
np.arange(3, 7, 2)
# array([3, 5])
```

**Linspace** is very similar, but with a slight twist. Linspace returns evenly spaced numbers over a specified interval. So given a starting and stopping point, as well as a number of values, linspace will evenly space them out for you in a NumPy array. This is especially helpful for data visualizations and declaring axes when plotting.

```python
# np.linspace(start, stop, num)
np.linspace(2.0, 3.0, num=5)
# array([ 2.0,  2.25,  2.5,  2.75, 3.0])
```
