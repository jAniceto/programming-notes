# Virtual enviroments

### Virtual environment using **virtualenv**
Install: `$ pip install virtualenv`

#### Create a new virtual enviroment: 

My prefered method is to create the environment in the respective project folder and naming it **venv**. Another alternative is to have a folder where you place all your virtualenvironments and name them according to their respective project.
```
$ cd desired_folder
$ virtualenv venv 
```

#### To activate the environment:

(Windows) `$ venv/Scripts/activate.bat`

(Linux) `$ source venv/bin/activate` 

Once activated you can normaly use **pip** to install packages in this environment: `$ pip install blabla`

You can see the list of installed packages using: `$ pip list`

To transfer the environment to another machine you can use: `$ pip freeze > requirements.txt` 

This will create a requirements.txt file, which contains a simple list of all the packages in the current environment, and their respective versions. Later, if you need to re-create the environment, install the same packages using the same versions: `$ pip install -r requirements.txt`


#### To deactivate the environment:

(Windows) `$ venv/Scripts/deactivate.bat`

(Linux) `$ deactivate`

