# Jupyter Notebooks

**Jupyter Notebook** is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

**JupyterLab** is the next-generation user interface for Project Jupyter. It offers all the familiar building blocks of the classic Jupyter Notebook (notebook, terminal, text editor, file browser, rich outputs, etc.) in a flexible and powerful user interface.

## Setup Jupyter Notebook

Install Jupyter Notebook with the following command. Alternatively, it is already packaged and ready to use with the Anaconda distribution.

```
pip install jupyter
```

Starting the Notebook Server:
```
jupyter notebook
```

Open a specific Notebook:
```
jupyter notebook notebook.ipynb
```

## Setup JupyterLab

Install JupyterLab with the following command.

```
pip install jupyterlab
```

Launch by running:
```
jupyter lab
```

## Useful IPython commands

The `%matplotlib inline` command is an IPython magic function that sets the output of plotting commands to be displayed inline within frontends like the Jupyter notebook, directly below the code cell that produced it. The resulting plots will then also be stored in the notebook document.

```
%matplotlib inline
```

The `figsize` sets the figure size

```
from IPython.core.pylabtools import figsize

figsize(10, 12)
```

Globaly set the scale of text and font for Seaborn

```
import seaborn as sns
sns.set(font_scale=2, font='Palatino Linotype')
```

## Add parent folder to path

This is useful so you can import into the notebook utility functions from a parent directory.

```python
# Add parent directory to Python path
import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

# Import function fun1 from modeule file1 in directory utils
from utils.file1 import fun1
```

## References

[JupyterLab Documentation](https://jupyterlab.readthedocs.io/en/stable/index.html)
