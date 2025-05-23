# Working with paths in Python using `pathlib`

`pathlib` is a Python Standard Library module created to make it easier to work with paths in a file system. This module debuted in Python 3.4 and updated in Python 3.5.

## The anatomy of a `pathlib.Path` on Windows
```python
from pathlib import Path

path = Path(r'C:/Users/Me/projects/blog/config.tar.gz')

path.drive
# 'C:'

path.root
# '/'

path.root
# 'C:/'

path.parent
# WindowsPath('C:/Users/Me/projects/blog')

path.name
# 'config.tar.gz'

path.stem
# 'config.tar'

path.suffix
# '.gz'

path.suffixes
# ['.tar', '.gz']
```

## Working with paths

### Creating paths and directories

When we convert a `WindowsPath` to string, Python adds backslashes. `repr` returns the path with forward slashses as it is represented on Windows.
```python
path = Path(r'C:/Users/Me/projects/blog/config.tar.gz')

str(path)
# 'C:\\Users\\Me\\projects\\blog\\config.tar.gz'

repr(path)
# "WindowsPath('C:/Users/Me/projects/blog/config.tar.gz')"
```

Creating and joining paths:
```python
Path('.', 'projects', 'python', 'source')
# WindowsPath('projects/python/source')

Path('.', 'projects', 'python') / Path('source')
# WindowsPath('projects/python/source')

Path('.', 'projects', 'python') / 'source'
# WindowsPath('projects/python/source')
```

Creating directories:
```python
path = Path('new_directory')
path.mkdir()

path.exists()
# True
```

When you have a directory path and it already exists, Python raises `FileExistsError` if you call `Path.mkdir()` on it.

Create parent directories recursively if not exists:
```python
path = Path('new_parent_dir/sub_dir')
path.mkdir(parents=True)
```

### List all files and directories
List all files and and directories:
```python
path = Path('/home/Me/projects/pathlib')
list(path.iterdir())
```

List only directories:
```python
[p for p in path.iterdir() if p.is_dir()]
```

List only files:
```python
[p for p in path.iterdir() if p.is_file()]
```


## References

- [Python pathlib Cookbook: 57+ Examples to Master It (2021)](https://miguendes.me/python-pathlib)
