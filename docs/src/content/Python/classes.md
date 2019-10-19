Title: Classes and OOP (Object Oriented Programming)
Date: 2017-09-13 14:36
Authors: José Aniceto
Modified: 2018-04-24 13:13


```python
class Foo:
    a = 0  # <-- class variable

    def __init__(self, b=0):
        self.b = b  # <-- instance variable

    def bar(self):  # <- instance method
        return self.a + self.b

    @classmethod
    def foo(cls, c=12):  # <-- class method
        return cls(c).bar()

def foobar():   # <-- function
    print(Foo.foo())
```

A function and a method are not the same thing, and a class and an instance are not the same thing, which is why a class variable/method and an instance variable/method are very definitely not the same things.

A class is like a blueprint, it tells you about some thing you want to make. An instance is the thing that gets made. 

For example, if you write up a blueprint for an airplane, the blueprint is like when you define a class. The airplanes that get made from that blueprint are like instances of a class. 

Defining a class looks like this:

```python
class Airplane:
  pass  
```

(Normally you would have some more code instead of `pass`. I'll explain that later.)
 
Now once you define a class you can create instances of a class like this, `Airplane()`. For example,

```python
airplane1 = Airplane()
airplane2 = Airplane()
```

Here we created two instances of the Airplane class and put them in the variables `airplane1` and `airplane2`. The important thing here is that you can change `airplane1` without affecting `airplane2`. They're two separate instances.

Okay now let's go back and talk about what goes inside a class. Let's take our Airplane class and fill it out:
```python
class Airplane:
    def __init__(self):
        print "A new instance got made!"
```
So what's going on here? `__init__` is a function that gets run when you create an instance. That's it! So if you go back to where we created the two Airplane instances,
```python
airplane1 = Airplane()
airplane2 = Airplane()
```

what would happen is, "A new instance got made!" would be printed out twice.

What about the `self` parameter? I think this would be easier to understand if we added a new method.

```python
class Airplane:
    def __init__(self):
        print "A new instance got made!"
    def fly(self):
        print "I'm flying!"
```

So if you wanted to call this method you'd do something like this: `airplane1.fly()`. Actually this is the same thing as this: `Airplane.fly(airplane1)`. Both of these would do the same thing, i.e. print out "I'm flying!". So `airplane1` is the instance that we used to call our `fly` method. This instance is what gets passed to `self`. 


### Classes

```python
# Function, this lives outside a class
def add(a, b):
    return a + b


class Adder():

    # __init__ roughly equivilant to a constructor in other languages
    def __init__(self, a, b):
        # Adding attributes to this instance of our class
        self.a = a
        self.b = b

    # Method, This belongs to an instance of a class and must have self as first argument. self refers to an instance of a class
    def add(self):
        return self.a + self.b

    # CLass Method, belongs to a class and is shared by every instance of the class, must have the class as first argument
    @classmethod
    def class_add(cls, x, y):
        return x + y

    # Static Method, Only belongs to the class for organisation, can't reference class or instance attributes
    @staticmethod
    def static_add(c, d):
        return c + d


# Let's start with an instance initialized with values for a and b
foo = Adder(1, 2)
# we call the add method of foo which refernces the values we initialized the class with
print ('Instance result', foo.add())

# Class method doesnt require an instance, note no () after Adder, we arent creating an instance, just referencing the class
bar = Adder.class_add(1, 2)
print ('Class result', bar)

# Static, similar to classmethod we don't need to create an instance
baz = Adder.static_add(1, 2)
print ('Static result', baz)

# Finally we'll just use our add function
spam = add(1, 2)
print ('Function result', spam)
```


### References:
* [https://www.reddit.com/r/learnpython/comments/1cpu7x/explain_classes_init_and_self_like_im_five/](https://www.reddit.com/r/learnpython/comments/1cpu7x/explain_classes_init_and_self_like_im_five/)
