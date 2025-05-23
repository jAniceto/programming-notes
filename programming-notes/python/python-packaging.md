# Python packaging

## Creating a `setup.py`

Example of a `setup.py` file:

```python
from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="marc",
    version="22.5.0",
    url="https://github.com/maxhumber/marc",
    description="Markov chain generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Max Humber",
    author_email="max.humber@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=[""],
    package_dir={"": "python/src"},
    extras_require={
        "dev": [
            "black>=22.3.0",
        ],
    },
    python_requires=">=3.9",
    setup_requires=["setuptools>=62.1.0"],
)
```

## Structure of package with CLI scripts

Example structure:

```
my_package/
    my_package/
        __init__.py
        cli_scripts.py
    setup.py
```

Let's assume your `__init__.py` looks like this (as a side note, I'd recommend moving the classes defined in there to a separate file, and then simply importing that file in the `__init__`):

```python
class Test(object):

    def __init__(self, a)
        self.a = a

    def __call__(self):
        print(self.a)
```

Now there is an additional file inside the package that utilizes the stuff you implemented in the package, let's call it `cli_scripts.py`:

```python
import argparse

from my_package import Test

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("a", type=int, help="Just an example argument")
    return parser.parse_args()

def demonstration():
    args = parse_args()
    t = Test(a=args.a)
    t()
```
My suggestion now is to utilize the `console_scripts` entry point inside `setup.py`, which could now look something like this:

```python
from setuptools import setup

setup(
    name='testpy',
    version='0.1',
    description='Just an example',
    author='RunOrVeith',
    author_email='xyz@mailinator.com',
    packages=["my_package"],
    entry_points={
        "console_scripts": ["mypkg=my_package.cli_scripts:demonstration"]},
    install_requires=[],
)
```
Now when you run `pip install .` inside the top-level `my_package` folder, your package will be installed. The `entry_points` automatically generate an executable for you, that you can now call with the name you gave it inside `setup.py`, in this example `mypkg`. This means you can now run `mypkg 5` and this will call `demonstration()`.

This way:

- you do not need to handle any `__main__` files
- you can give your script a meaningful name
- you don't need to care whether your script is executable, or specify to run the script with python
- you can have as many of these as you want inside the list `entry_points`
- it forces you to write functions that you could also call from other modules, instead of the `__main__`
