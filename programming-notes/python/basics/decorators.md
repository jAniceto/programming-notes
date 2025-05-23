# Decorators

Decorators are wrappers around a function that modify the behavior of the function in a certain way. Let’s create our own decorator:

```python
def print_argument(func):
    def wrapper(the_number):
        print("Argument for", 
              func.__name__, 
              "is", the_number)
        return func(the_number)
    return wrapper
@print_argument
def add_one(x):
    return x + 1
print(add_one(1))
```

Inside `print_argument`, we define a wrapper function. This function prints the argument and the name of the called function. Next, it executes the actual function and returns its result as if the function was called regularly. With `@print_argument` we apply our decorator to a function. The output of our little script will be:

```python
# Argument for add_one is 1
# 2
```
