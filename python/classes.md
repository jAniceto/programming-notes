# Classes and OOP (Object Oriented Programming)


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


### References:
* [https://www.reddit.com/r/learnpython/comments/1cpu7x/explain_classes_init_and_self_like_im_five/](https://www.reddit.com/r/learnpython/comments/1cpu7x/explain_classes_init_and_self_like_im_five/)
