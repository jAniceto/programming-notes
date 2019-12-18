Title: Argument parsing using the argparse module
Date: 2019-11-22 17:47
Authors: José Aniceto


**argparse** is a Python Standard Library module to write user-friendly command-line interfaces. The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv. The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments



### Initialize

```python
import argparse

# Instantiate the parser
parser = argparse.ArgumentParser(description='Optional app description')
```

### Add Arguments

```python
# Required positional argument
parser.add_argument('pos_arg', type=int,
                    help='A required integer positional argument')

# Optional positional argument
parser.add_argument('opt_pos_arg', type=int, nargs='?',
                    help='An optional integer positional argument')

# Optional argument
parser.add_argument('--opt_arg', type=int,
                    help='An optional integer argument')

# Switch
parser.add_argument('--switch', action='store_true',
                    help='A boolean switch')
```

### Parse

```python
args = parser.parse_args()
```

### Access

```python
print("Argument values:")
print(args.pos_arg)
print(args.opt_pos_arg)
print(args.opt_arg)
print(args.switch)
```

### Check Values

```python
if args.pos_arg > 10:
    parser.error("pos_arg cannot be larger than 10")
```

### Usage

Assuming the Python code above is saved into a file called `prog.py`.

#### Correct use:

```
$ python prog.py 1 2 --opt_arg 3 --switch

Argument values:
1
2
3
True
```

#### Incorrect arguments:

```
$ python prog.py foo 2 --opt_arg 3 --switch
usage: convert [-h] [--opt_arg OPT_ARG] [--switch] pos_arg [opt_pos_arg]
prog.py: error: argument pos_arg: invalid int value: 'foo'

$ python prog.py 11 2 --opt_arg 3
Argument values:
11
2
3
False
usage: python prog.py [-h] [--opt_arg OPT_ARG] [--switch] pos_arg [opt_pos_arg]
convert: error: pos_arg cannot be larger than 10
```

#### Full help
```
$ python prog.py -h
```


### References:

- [Python docs](https://docs.python.org/3/library/argparse.html)
- [Stack Overflow answer](https://stackoverflow.com/a/30493366)
