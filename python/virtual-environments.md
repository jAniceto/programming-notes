# Virtual enviroments

## Main packages to handle virtual environments
- [venv (Standard Library)](#venv-(standard-library))
- [Pipenv](#pipenv)
- [virtualenv](#virtualenv-package)
- [Poetry](#poetry)


## venv (Standard Library)

`venv` already comes with the Python Standard Library so no installation is required.

### Create a new virtual enviroment: 

To create a new virtual environment: `$ python -m venv env_name`

A new folder appears in your current location containinng the new Python installation. The environemnt uses the same Python version as the one used to create it.

To activate the virtual environment: `$ env_name/Scripts/activate.bat`

Once the virtual environment is activated, when you install a package with `pip install package`, it will only be installed in the environment.

To deactivate the virtual environment: `$ deactivate`

To create a requirements file for your project: `$ pip freeze > requirements.txt`

To delete the virtual environment completly just delete the enviroment folder (`env_name`) or run: `$ rmdir env_name /s`

To install packages from an existing `requirements.txt` file: `pip install -r requirements.txt`

Create a virtual environment with access to the packages in the global installation of Python: 

`$ python -m venv env_name --system-site-packages`



## Pipenv

Installing Pipenv: `$ pip install pipenv`

To upgrade Pipenv at any time run: `$ pip install --upgrade pipenv`

### Installing packages for your project
```
$ cd myproject
$ pipenv install requests
```
Pipenv will install the excellent Requests library and create a Pipfile for you in your project’s directory. The Pipfile is used to track which dependencies your project needs in case you need to re-install them, such as when you share your project with others.

To install as a dev dependency run:
```
$ pipenv install -dev requests
```

To remove an installed package run:
```
$ pipenv uninstall requests
```

### Using installed packages

Import your packages normally in your scripts. Then you can run the script using `pipenv run`:

```
$ pipenv run python main.py
```

Using `$ pipenv run` ensures that your installed packages are available to your script. 

It's also possible to spawn a new shell that ensures all commands have access to your installed packages with `$ pipenv shell`.
```
$ pipenv shell
(env-name) $ python main.py
```

### Other commands:
* `pipenv --rm`: Removes the virtual environment completly
* `pipenv --python 3.6.5`: Specify Python version
* `pipenv --venv`: Shows virtual environment path
* `pipenv graph`: Dependencies tree
* `pipenv install --dev -e .`: Install as editable

### Set enviromental variables

Create a `.env` file at the root folder of the project, next to the `Pipfile`. Add enviromental variables like so:
```
MY_TOKEN=SuperToKen
MY_VAR=SuperVar
```

You can add comments in this file with a leading `#`. This file will be loaded automatically with `pipenv shell` or `pipenv run your_command` and the environment variables will be available.

You can access/check them in your code with:
```python
print(os.getenv('MY_TOKEN', 'Token Not found'))
```

Note: Remember to exclude this file from your version control.

### References
- [Pipenv Documentation](https://pipenv.readthedocs.io/en/latest/)
- [Pipenv playground](https://rootnroll.com/d/pipenv/)


## virtualenv package

Install: `$ pip install virtualenv`

### Create a new virtual enviroment: 

My prefered method is to create the environment in the respective project folder and naming it **venv**. Another alternative is to have a folder where you place all your virtualenvironments and name them according to their respective project.
```
$ cd desired_folder
$ virtualenv venv 
```

### To activate the environment:

(Windows) `$ venv/Scripts/activate.bat`

(Linux) `$ source venv/bin/activate` 

Once activated you can normaly use **pip** to install packages in this environment: `$ pip install blabla`

You can see the list of installed packages using: `$ pip list`

To transfer the environment to another machine you can use: `$ pip freeze > requirements.txt` 

This will create a requirements.txt file, which contains a simple list of all the packages in the current environment, and their respective versions. Later, if you need to re-create the environment, install the same packages using the same versions: `$ pip install -r requirements.txt`


### To deactivate the environment:

(Windows) `$ venv/Scripts/deactivate.bat`

(Linux) `$ deactivate`


## Poetry

Poetry not only handles dependenct management through virtual environments but also has several other features like pachaging.

### Install

The recommended way to install Poetry on Windows is via Powershell:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```
You only need to install Poetry once. It will automatically pick up the current Python version and use it to create virtualenvs accordingly.

To compleatly uninstall Poetry run:

```powershell
python get-poetry.py --uninstall
```

or 

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py - --uninstall
```

### Usage

To create a new project run named `poetry-demo`:
```
poetry new poetry-demo
```
This will create the `poetry-demo` directory with the following content:
```
poetry-demo
├── pyproject.toml
├── README.rst
├── poetry_demo
│   └── __init__.py
└── tests
    ├── __init__.py
    └── test_poetry_demo.py
```

To **add or modify dependencies** you can edit the `pyproject.toml` file. Alternatively you can add a dependency by running:
```
poetry add package_name
```
To add to dev packages run:
```
poetry add package_name --dev
```
By default, Poetry creates a virtual environment in `{cache-dir}\virtualenvs` on Windows.

To run your script user:
```
poetry run python your_script.py
OR
poetry run pytest
```

To **activate the virtual environment** create a poetry shell with:
```
poetry shell
```

To deactivate the virtual environment and exit this new shell type `exit`

To **install** the defined dependencies for your project: 
```
poetry install
```

To list all of the available packages:
```
poetry show
```

To create a `pip` style `requirements.txt` file (including dev dependencies)
```
poetry export -f requirements.txt --output requirements.txt --dev --without-hashes
```

