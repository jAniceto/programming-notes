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

Rollback Anaconda environment

Sometimes updating your environment can bring unintended consequences. Fortunatly Anaconda allows you to list the changes to your environment and revert to a previous point.

List the history of each change to the current environment:

```
$ conda list --revisions
```

You'll get an output like this:

```
     ...
     
2020-06-24 12:47:58  (rev 12)
     _anaconda_depends  {2019.03 (defaults/win-64) -> 2020.02 (defaults/win-64)}
     astropy  {4.0 (defaults/win-64) -> 4.0.1.post1 (defaults/win-64)}
     atomicwrites  {1.3.0 (defaults/win-64) -> 1.4.0 (defaults/noarch)}
     autopep8  {1.4.4 (defaults/noarch) -> 1.5.3 (defaults/noarch)}
     backcall  {0.1.0 (defaults/win-64) -> 0.2.0 (defaults/noarch)}
     bcrypt  {3.1.7 (defaults/win-64) -> 3.1.7 (defaults/win-64)}
     beautifulsoup4  {4.8.2 (defaults/win-64) -> 4.9.1 (defaults/win-64)}
     bitarray  {1.2.1 (defaults/win-64) -> 1.2.2 (defaults/win-64)}
     ...
     xz  {5.2.4 (defaults/win-64) -> 5.2.5 (defaults/win-64)}
     yapf  {0.28.0 (defaults/noarch) -> 0.29.0 (defaults/noarch)}
     zipp  {2.2.0 (defaults/noarch) -> 3.1.0 (defaults/noarch)}
     zlib  {1.2.11 (defaults/win-64) -> 1.2.11 (defaults/win-64)}
     zstd  {1.3.7 (defaults/win-64) -> 1.4.4 (defaults/win-64)}
    -backports.os-0.1.1 (defaults/win-64)
    +brotlipy-0.7.0 (defaults/win-64)
    +importlib-metadata-1.6.1 (defaults/win-64)
    +prompt-toolkit-3.0.5 (defaults/noarch)
    +regex-2020.5.14 (defaults/win-64)
    +threadpoolctl-2.1.0 (defaults/noarch)
    +toml-0.10.1 (defaults/noarch)

2020-06-24 14:57:05  (rev 13)
    +plotly-4.8.1 (plotly/noarch)
    +retrying-1.3.3 (defaults/win-64)

2020-11-02 14:49:53  (rev 14)
     _anaconda_depends  {2020.02 (defaults/win-64) -> 2020.07 (defaults/win-64)}
     asn1crypto  {1.3.0 (defaults/win-64) -> 1.4.0 (defaults/noarch)}
     astroid  {2.3.3 (defaults/win-64) -> 2.4.2 (defaults/win-64)}
     astropy  {4.0.1.post1 (defaults/win-64) -> 4.0.2 (defaults/win-64)}
     attrs  {19.3.0 (defaults/noarch) -> 20.2.0 (defaults/noarch)}
     autopep8  {1.5.3 (defaults/noarch) -> 1.5.4 (defaults/noarch)}
     bcrypt  {3.1.7 (defaults/win-64) -> 3.2.0 (defaults/win-64)}
     ...
    +nest-asyncio-1.4.1 (defaults/noarch)
    +tifffile-2020.10.1 (defaults/win-64)
    +typed-ast-1.4.1 (defaults/win-64)
    +zope-1.0 (defaults/win-64)
    +zope.event-4.5.0 (defaults/win-64)
    +zope.interface-5.1.2 (defaults/win-64)
```

It list each revision along with updated packages (old version -> new version) and newly added packages (the ones with + symbol). Now you can safely rollback to previous versions of your environment by using `conda install -–revision revision number`. For instance:

```
conda install --revision 13
```



## References
- https://stackoverflow.com/a/37008663/5240904
- https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
