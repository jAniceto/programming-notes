# Jupyter Notebooks


## Instalation
```
pip install jupyter
```

## Usage

Starting the Notebook Server:
```
jupyter notebook
```

Open a specific Notebook:
```
jupyter notebook notebook.ipynb
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
