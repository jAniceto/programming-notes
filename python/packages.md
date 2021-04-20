# Python packages and modules

## Modules

A python “module” is a single namespace, with a collection of values:

- functions
- constants
- class definitions
- etc.

A module usually corresponds to a single file: `something.py`

## Packages

A package is essentially a module, except it can have other modules (and indeed other packages) inside it.

A package usually corresponds to a directory with a file in it called `__init__.py` and any number of python files or other package directories:

```
a_package
   __init__.py
   module_a.py
   a_sub_package
     __init__.py
     module_b.py
```

The `__init__.py` can be totally empty or it can have python code in it. The code will be run when the package is imported. Modules inside packages are not automatically imported. So, with the above structure:

```
import a_package
```

will run the code in `a_package/__init__.py`.

Any names defined in the `__init__.py` will be available in:

```
a_package.a_name
```

but:

```
a_package.module_a
```

will not exist. To get submodules, you need to explicitly import them:

```
import a_package.module_a
```

## Python packaging tools - `setuptools`

### The `setup.py` file

An example setup.py:

```
from setuptools import setup

 setup(
   name='PackageName',
   version='0.1.0',
   author='An Awesome Coder',
   author_email='aac@example.com',
   packages=['package_name', 'package_name.test'],
   scripts=['bin/script1','bin/script2'],
   url='http://pypi.python.org/pypi/PackageName/',
   license='LICENSE.txt',
   description='An awesome package that does something',
   long_description=open('README.txt').read(),
   install_requires=[
       "Django >= 1.1.1",
       "pytest",
   ],
)
```

### Running `setup.py`

With a `setup.py` script defined, setuptools can do a lot:

Build a source distribution (a tar archive of all the files needed to build and install the package):

```
python setup.py sdist
```

Build from source:

```
python setup.py build
```

And install:

```
python setup.py install
```

Install in "develop" or "editable" mode:
```
python setup.py develop
```
or
```
pip install -e .
```

## References

- [Making a Python Package](https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html)
- [https://packaging.python.org/](https://packaging.python.org/)
- [How To Package Your Python Code](https://python-packaging.readthedocs.io/en/latest/)
- [Sample Python Project](https://github.com/pypa/sampleproject)
