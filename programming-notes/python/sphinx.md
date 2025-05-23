# Creating documentation with Sphinx

## Set up

Install Sphinx:

```
pip install sphinx
```

Generate the basic structure of Sphinx documentation. It is usually recommended to separate source and build directories.

```
sphinx-quickstart docs
```

Now we can build the HTML documentation with:

```
cd docs/
.\make.bat html
```

Note: `.\make.bat html` is for Powershell. `make html` for macOS, Linux or Windows command prompt

Serve with Python built-in HTTP server:

```
python -m http.server
```

## Using Markdown with Sphinx

Convert RST files to Markdown:

```
pip install "rst-to-myst[sphinx]"
rst2myst convert docs/**/*.rst
```

We can now delete the index.rst file.

In the Sphinx `config.py` file we now need to add the following extension:

```
extensions = [
    "myst_parser",
]
```

and install it:

```
pip install myst-parser
```

Now we can build the HTML from the Markdown files.

```
cd docs/
make html
python -m http
```

## Useful configurations

To monitor changes in the docs and rebuild the HTML we can use `sphinx-autobuild`:

```
pip install sphinx-autobuild
sphinx-autobuild docs/source/ docs/build/html
```

If you wish to include the README.md file in the docs, in the docs/source/index.md add the following directive:


    ```{include} ../../README.md
    :relative-images:
    ```

To add a warning:

    ```{warning} 
    Warning text.
    ```

Other handy extensions:

```
extensions = [
    'myst_parser',
    'sphinx.ext.duration',
    'sphinx.ext.autosectionlabel',
]
```

Install another theme:

```
pip install furo
```

In the Sphinx `config.py`:

```
html_theme = 'furo'
```

Create a new page (`usage.md`) next to the `index.md` file. Link to a page:

```
Check page {doc}`usage`. 
Specifically the section {ref}`Instalation`.
```

## Creating module pages automatically

```rst
Joback Method
=============

.. automodule:: chem_eng_kit.properties.joback
    :members:
    :exclude-members: _sum_group_property
```

## Creating docstrings

### Code blocks

```python
def foo():
    '''
    .. highlight:: python
    .. code-block:: python

        res = aFunction(something, goes, in)
        print(res.avalue)
    '''
```

Inline code in reStructuredText:

```python
def foo():
    '''
    bla `foo()` bla
    '''
```

Inline code in Markdown:

```python
def foo():
    '''
    bla ``foo()`` bla
    '''
```

### Math 

Displayed math:

```python
def foo():
    '''
    .. math:: V_c [cm^3/mol] = 17.5 + \\sum V_{c,i}
    '''
```

Inline math:

```python
def foo():
    '''
    where :math:`N_{atom}` is the number of atoms
    '''
```
