# Anaconda

Anaconda is a distribution of the Python language aimed for scientific computing (data science, machine learning applications, large-scale data processing, predictive analytics, etc.). It aims to simplify package management and deployment. The distribution includes data-science packages suitable for Windows, Linux, and macOS.

## Managing enviroments

### Enviroments info
```
$ conda env list
```
or 
```
$ conda info --envs
```

### Create a new enviroment

Create an environment:
```
$ conda create --name venv_name
```

Create an environment with a specific version of Python: 
```
$ conda create -n venv_name python=3.6
```

To activate this environment:
```
$ conda activate venv_name
```

To deactivate an active environment:
```
$ conda deactivate
```

To remove an environment:
```
$ conda remove --name myenv --all
```

To specify the location of the new enviroment use:
```
$ conda create --prefix /tmp/test-env
```

### Create an enviroment from a file

Export your active environment to a new file:
```
$ conda env export > environment.yml
```

Create from `environment.yml`:
```
$ conda env create -f environment.yml
```
The first line of the `yml` file sets the new environment's name.


### Create a requirements file

To create an Anaconde requirements file use:
```
$ conda list -e > requirements.txt
```
Note: This `requirements.txt` is not compatible with `pip`. 

The resulting file can be used to create a conda virtual environment with:
```
$ conda create --name venv_name --file requirements.txt
```

However, this output isn't in the right format for `pip`. If you want a file which you can use to create a `pip` virtual environment you can install pip within the conda environment, the use pip to create `requirements.txt`.

```
$ conda activate venv_name
$ conda install pip
$ pip freeze > requirements.txt
```

### Clone an existing enviroment

For instance, to clone the base enviroment use:
```
$ conda create --name venv_name --clone base
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

## Set environment variables
To list any variables:
```
$ conda env config vars list
```

To set environment variables:
```
$ conda env config vars set my_var=value
```

Once you have set an environment variable, you have to reactivate your environment with `conda activate venv_name`. To check if the environment variable has been set, run `echo my_var` or `conda env config vars list`.

Declare environment variables in the `environment.yml`:
```
name: venv_name
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.7
  - codecov
variables:
  VAR1: valueA
  VAR2: valueB
```

## Rollback Anaconda environment

[Link](../data-analysis/rollback-anaconda.md)

## References
- https://stackoverflow.com/a/37008663/5240904
- https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
