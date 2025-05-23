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

To remove packages:

```
$ uv remove flask
```

Working with development dependencies:

```
$ uv add --dev black
$ uv run black path\to\file.py
```


## Running scripts

To run python files in you environment use:

```
$ uv run example.py
```


## Working with tools

Tools are pacakges that can perform several functions but are not part of your project. For instance, it is common to use a linter/formatter when developing (e.g., `ruff`). With `uv` you can use tools like `ruff` in different ways.

### Ways to use tools

1) Running a tool without installing it (it's installed in a temporary environment and deleted after use).  
  ```
  $ uv tool run ruff check
  ```
  The following alias can also be used and results in the same:
  ```
  $ uvx ruff check
  ```

2) When a tool is used frequently it may be usefull to install it to a persistent environment and add it to the `PATH`.
  ```
  $ uv tool install ruff
  ```
  Now, whatever the project you are wirking in, you can run `ruff` by doing:
  ```
  $ ruff check
  ```

3) You can also install the tool in your project as a development dependency
  ```
  $ uv add --dev ruff
  ```
  And run it with
  ```
  $ uv run ruff check
  ```

### Upgrading tools

Upgrade all tools with:
```
$ uv tool upgrade --all
```

Or a single tool with:
```
$ uv tool upgrade ruff
```



## Working with `jupyter`

If you're working within a project, you can start a Jupyter server with access to the project's virtual environment by:
```
$ uv run --with jupyter jupyter lab
```

Alternatively you can install Jupyter as a dev dependency in your project
```
$ uv add --dev jupyterlab
$ uv run jupyter lab
```


## Project entry points and command line interfaces

To create a project CLI you need to configure entry point tables in the `pyproject.toml` and add a build system. For example, to declare a command called `hello` that invokes the `hello` function in the `example` module:

In the `pyproject.toml` file:

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project.scripts]
hello = "example:hello"
```

You can then run the command with:
```
$ uv run hello
```


## Deploying

Deploying the project to production excluding dev dependencies:

```
$ uv sync --no-dev
```

## References

- [uv Documentation](https://docs.astral.sh/uv/)
