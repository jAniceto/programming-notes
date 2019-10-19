Title: *args and **kwargs
Date: 2017-10-13 11:58
Authors: José Aniceto


### A normal function: 

```python
def func1(one, two)
  print(one)
  print(two)

func1('arg one', 'arg two')  # Correct
func1('arg one')  # Error
func1('arg one', 'arg two', 'arg three')  # Error
```

### *args usage:

```python
def func2(*args)
  for stuff in args:
    print(stuff)
    
my_list = ['green', 'yellow', 'blue', 'red']

func2(*my_list)  # Correct
func2('green', 'yellow', 'blue', 'red')  # Correct
```


```python
def func3(one, two, *args)
  print(one)
  print(two)
  for stuff in args:
    print(stuff)
    
my_list = ['green', 'yellow', 'blue', 'red']

func3('required one', 'required two', *my_list)  # Correct
```


### **kwargs usage:

```python
def func4(**kwargs)
  for key, value in kwargs.items():
    print(key)
    print(value)
    
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

func4(**kwargs)  # Correct
func4(key1 = 'value1', key2 = 'value2', key3 = 'value3')  # Correct
```
