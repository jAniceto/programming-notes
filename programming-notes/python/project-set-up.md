# Project set-up

## Setting a project with Git, Poetry and Pycharm

1) Initialize a Git Repository something like the Github Desktop App or using Git by running:

```
$ git init your_project_name
```

2) Create a `.gitignore` file and add all relevant exclusions. You can use something like [toptal.com/developers/gitignore](https://www.toptal.com/developers/gitignore). Here is an example `.gitignore` for [Python, Pycharm, and Windows](https://www.toptal.com/developers/gitignore/api/windows,pycharm,jupyternotebooks,python).


3) Set up Poetry:

```
$ cd your_project_name
$ poetry init
```

Follow the prompts to set up your project. This will create a `pyproject.toml` file.

4) Install Dependencies:

For example, to add requests as a dependency:

```
$ poetry add requests
```

To create a Virtual Environment: `$ poetry shell`.

5) Pycharm

Open Pycharm and open the project folder. 
Then, configure the Python interpreter by selecting the one create by Poetry.
