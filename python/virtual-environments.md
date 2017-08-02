# Virtual enviroments

### Virtual environment using **virtualenv**
Install: `pip install virtualenv`

##### Create a new virtual enviroment: 

My prefered method is to create the environment in the respective project folder and naming it **venv**. Another alternative is to have a folder where you place all your virtualenvironments and name them according to their respective project.
```
cd desired_folder
virtualenv venv 
```

##### To activate the environment:

(Windows) `venv/Scripts/activate.bat`

(Linux) `source venv/bin/activate`

##### To deactivate the environment:

(Windows) `venv/Scripts/deactivate.bat`

(Linux) `deactivate`
