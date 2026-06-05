# Ruff - Python linter and code formatter

## Installing

Ruff can be invoked directly with `uvx`:

```bash
$ uvx ruff check   # Lint all files in the current directory.
$ uvx ruff format  # Format all files in the current directory.
```

This runs `ruff` as a `uv` tool without installing it (it's installed in a temporary environment and deleted after use).

Alternatively you can install with `uv` (recommended):

To install Ruff globally.

```bash
$ uv tool install ruff@latest
```

## Usage

### Lint

```bash
$ ruff check                  # Lint files in the current directory.
$ ruff check --fix            # Lint files in the current directory and fix any fixable errors.
$ ruff check --watch          # Lint files in the current directory and re-lint on change.
$ ruff check path/to/code/    # Lint files in `path/to/code`.
```

For the full list of supported options, run `ruff check --help`.


### Formatter

```bash
$ ruff format                   # Format all files in the current directory.
$ ruff format path/to/code/     # Format all files in `path/to/code` (and any subdirectories).
$ ruff format path/to/file.py   # Format a single file.
```

For the full list of supported options, run `ruff format --help`.


### Sorting imports

```bash
$ ruff check --select I --fix
$ ruff  format
```
