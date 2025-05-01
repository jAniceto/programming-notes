# Working with uv

`uv` is a Python package and project manager. It is extremely fast, compared with alternatives.


## Installing 

On Windows, you can install `uv` using Powershell:

```
$ powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

More info on other installation options can be found on the [uv docs](https://docs.astral.sh/uv/getting-started/installation/).

To update uv:

```
$ uv self update
```


## Starting a new project

Starting a project with `uv`:

```
$ uv init project_name
```

`uv` creates a new directory called `project_name` and sets up a few project files. You can then enter the project folder.

```
$ cd project_name
```

Note: If you already have a project folder you can ask `uv` to initialize the project there:

```
$ cd project_name
$ uv init
```

When starting a new project you can specify the Python version using:

```
$ uv init project_name --python 3.11
```

## Installing packages

To add packages:

```
$ cd project_name
$ uv add requests flask
```

Working with development dependencies:

```
$ uv add --dev black
$ uv run black path\to\file.py
```

## Deploying

Deploying the project to production excluding dev dependencies:

```
$ uv sync --no-dev
```

## References

- [uv Documentation](https://docs.astral.sh/uv/)
