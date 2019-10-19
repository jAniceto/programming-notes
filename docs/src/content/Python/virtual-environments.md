Title: Virtual enviroments
Date: 2017-08-02 22:57
Authors: José Aniceto
Modified: 2018-12-15 01:51

## Pipenv

Installing Pipenv: `$ pip install pipenv`

To upgrade Pipenv at any time run: `$ pip install --upgrade pipenv`

### Installing packages for your project
```
$ cd myproject
$ pipenv install requests
```
Pipenv will install the excellent Requests library and create a Pipfile for you in your project’s directory. The Pipfile is used to track which dependencies your project needs in case you need to re-install them, such as when you share your project with others.

### Using installed packages

Import your packages normally in your scripts. Then you can run the script using `pipenv run`:

```
$ pipenv run python main.py
```

Using `$ pipenv run` ensures that your installed packages are available to your script. It’s also possible to spawn a new shell that ensures all commands have access to your installed packages with `$ pipenv shell`.



Documentation: [Pipenv](https://pipenv.readthedocs.io/en/latest/)

---

## Virtual environment using **virtualenv**
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

