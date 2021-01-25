# Anaconda

Anaconda is a distribution of the Python language aimed for scientific computing (data science, machine learning applications, large-scale data processing, predictive analytics, etc.). It aims to simplify package management and deployment. The distribution includes data-science packages suitable for Windows, Linux, and macOS.

## Managing enviroments

### Create a new enviroment

```
$ conda create --name venv
```

To activate this environment, use
```
$ conda activate full/path/venv
```

To deactivate an active environment, use
```
$ conda deactivate
```

To specify the location of the new enviroment use:
```
$ conda create --prefix /tmp/test-env
```

### Creating a requirements file

To create an Anaconde requirements file use:
```
$ conda list -e > requirements.txt
```

The resulting file can be used to create a conda virtual environment with:
```
$ conda create --name <env_name> --file requirements.txt
```

However, this output isn't in the right format for `pip`. If you want a file which you can use to create a `pip` virtual environment you can install pip within the conda environment, the use pip to create `requirements.txt`.

```
$ conda activate <env>
$ conda install pip
$ pip freeze > requirements.txt
```

### Clone an existing enviroment

For instance, to clone the base enviroment use:
```
$ conda create --name <env_name> --clone base
```

## Add a folder to the Anaconda path

By adding a folder to the Anaconda path you can call its Python scripts from any location in the Anaconda Prompt. 

```
cd your_folder
conda-develop .
```

or 

```
conda-develop /path/to/module/
```

## References
- https://stackoverflow.com/a/37008663/5240904
- https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
