# Argument parsing using the argparse module

## argparse

**argparse** is a Python Standard Library module to write user-friendly command-line interfaces. The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv. The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments



### Initialize

```python
import argparse

# Instantiate the parser
parser = argparse.ArgumentParser(prog='Optional app name', 
                                 description='Optional app description', 
                                 epilog='Enjoy the program!')
```

By default, the **argparse** uses the value of the sys.argv[0] element to set the name of the program (name of the Python script). However, you can specify the name of your program just by using the `prog` keyword.

You can customize the text displayed before and after the arguments help text using the `description` and `epilog` keywords.

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

## Subcommands
Many programs split up their functionality into a number of sub-commands. You can create the sub-commands with the `add_subparsers()` method. Here is an example of a CLI names `program.py`.


```python
import argparse

# Create the parser
parser = argparse.ArgumentParser(prog='argparseCLI', description='argparse CLI')
subparsers = parser.add_subparsers(dest='command', help='sub-command help')

# Subparser for sum command
subparser_sum = subparsers.add_parser('sum', help='sum help')
subparser_sum.add_argument('num1', type=int, help='num 1')
subparser_sum.add_argument('num2', type=int, help='num 2')

# Subparser for hi command
subparser_hi = subparsers.add_parser('hi', help='hi help')
subparser_hi.add_argument('name', type=str, help='Name')

# Parse arguments
args = parser.parse_args()

# Run
if args.command == 'sum':
    print(args.num1 + args.num2)
elif args.command == 'hi':
    print(f'Hi {args.name}')
```

You use it like so:

```shell
$ python program.py sum 1 3
4

$ python program.py hi John
Hi John

$ python program.py sum John
usage: program sum [-h] num1 num2
argparseCLI sum: error: argument num1: invalid int value: 'John'
```


## `Argh`: wrapper to simplify argparse

```python
import argh

def do_the_thing(required_arg, optional_arg=1, other_optional_arg=False):
    """
    I am a docstring
    """
    print((required_arg, type(required_arg)))
    print((optional_arg, type(optional_arg)))
    print((other_optional_arg, type(other_optional_arg)))


@argh.arg('--bool-arg-for-flag', '-b', help="Flip this flag for things")
@argh.arg('arg_with_choices', choices=['one', 'two', 'three'])
def do_the_other_thing(arg_with_choices, bool_arg_for_flag=False):
    print(arg_with_choices)
    print(bool_arg_for_flag)


if __name__ == '__main__':
    # argh.dispatch_command(do_the_thing)
    argh.dispatch_commands([do_the_thing, do_the_other_thing])
```

### References:

- [Python docs](https://docs.python.org/3/library/argparse.html)
- [Stack Overflow answer](https://stackoverflow.com/a/30493366)
- [Real Python - How to Build Command Line Interfaces in Python With argparse](https://realpython.com/command-line-interfaces-python-argparse/)
- [Argh](https://github.com/neithere/argh/)
