Title: Progress Bars
Date: 2018-02-28 16:59
Authors: José Aniceto


## Basic progress bar

There are many progressbars out there for Python, but they are dependencies, and this can be really annoying, especially when it is hard to install pip libraries.

To make any progressbar, you need to know the string option `\r`. What makes `\r` unique is that it will go to the start of printing.

For example, if you were to do `print('Hello World!')`, it would print Hello World!. To visualize it, it is more like

```
Hello World!
            ^
```
The cursor is at the character after the !. If we were to use `\r`, the cursor would go to the front. In our example, it would mean

```
Hello World!
^
```
See how the cursor is at the h? If it were to print anything, it would overwrite the character h.

Theoretically, if we want to make a progressbar, we have to print a string multiple times with `\r`.

```python
times = 1 # how many times the loop has looped
for i in range(10): # will repeat whatever is below 10 times.
    print('\rHappened '+str(times)+' times.') #happened x times
    times += 1 #this is the same as times = times + 1
```

However, if we run this, there will be an error. Each line will print on a new line.

```
Happened 1 times.
Happened 2 times.
Happened 3 times.
Happened 4 times.
Happened 5 times.
Happened 6 times.
Happened 7 times.
Happened 8 times.
Happened 9 times.
Happened 10 times.
```

This is because the print function adds `\n` to the end of every string that is printed. Theoretically, it is printing `'\rHappened '+str(times)+' times.\n'`. We do not want `\n` to be added, so to fix this, write `print('\rHappened '+str(times)+' times.', end = '')`. This makes it so that print will add `''` to the end of every string, which is equal to nothing. Finally if you run

```python
times = 1 # how many times the loop has looped
for i in range(10): # will repeat whatever is below 10 times.
    print('\rHappened '+str(times)+' times.', end = '') #happened x times
    times += 1 #this is the same as times = times + 1
```
You will get just one line of text. The only problem is that it happens so quickly, that you cannot see the bar updating. Try making it loop 1000000 times.

```python
times = 1 # how many times the loop has looped
for i in range(1000000): # will repeat whatever is below 1000000 times.
    print('\rHappened '+str(times)+' times.', end = '') #happened x times
    times += 1 #this is the same as times = times + 1
```
Now you can see the text changing.

Finally, you want to make sure to run `times = 1` every time you use this progressbar so that the number restarts at 1. You can also change the text to say whatever you want.

To do a basic x/total bar, just add a bit of text that says the total:
```python
times = 1 # how many times the loop has looped
for i in range(1000000): # will repeat whatever is below 1000000 times.
    print('\rHappened '+str(times)+'/1000000 times.', end = '') #happened x times
    times += 1 #this is the same as times = times + 1
```

For basic programmers:
```python
def basic_function():
    sum = 1+1

def counter(reps):
    times = 1
    for i in range(reps): # will repeat whatever is below reps times.
        basic_function()
        print('\rHappened '+str(times)+'/'+str(reps)+' times.', end = '') #happened x times
        times += 1 #this is the same as times = times + 1

counter(1000000)
```

Just replace whatever is in basic_function with whatever you want to happen

If you are on Python2, enter in from `__future__ import print_function` at the top of the file/first thing on your interpter

## Using [tqdm](https://github.com/tqdm/tqdm) library

```python
from tqdm import tqdm

alist = list(range(5))

for thing in tqdm(alist):
    print(thing)  # or whatever you do...
```
