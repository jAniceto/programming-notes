# Git Version Control System

## Instalation 

On a Debian-based distribution, such as Ubuntu

```
$ sudo apt update
$ sudo apt install git-all
```

On Windows download and install from [git-scm.com](https://git-scm.com/download/win).

Configure your user name and email address:

```
$ git config --global user.name "exampleusername"
$ git config --global user.email "example@gmail.com"
```

## Creating repositories 

### Create a new local repository

```git
$ cd path/to/desired/directory
$ git init
```

### Clone an existing repository

Grab the `https` or `ssh` path from the remote (Github, GitLab, etc...) and then run:

```git
$ git clone ssh://user@domain.com/repo.git
```

## Working locally

Check the status of our repository:

```git
$ git status
```

When we create a new file `git` becomes aware of it but it is still not tracking changes to that file. To instruct `git` to track a file run:

```git
$ git add file1.txt
```

Now `git` is tracking the file but changes haven't been recorded as a commit yet. A commit is a record of a change. This change will be permanently recorded in our history, and can be reverted to at a later date. To make a commit we use `git commit`. We also add a message which should be a short desciption of changes made.

```git
$ git commit -m "Added stuff on file 1"
```

The `-m` flag allows us add a short message to each commit. A good commit message should give a brief statement of any changes made to the file.

To commit all local changes in tracked files (however this is generally discouredged):
  
```git
$ git commit -a -m "Changed something"
```

We can lookup recent changes made to our repository with:

```git
$ git log
```


## Working with remote repository

To push your local changes to the remote repository we use the following command:

```git
$ git push origin master
```

To pull the current version of the repository from the remote server use:

```git
$ git pull
```

If your default branch is different than master, you will need to specify the branch name:

```
$ git pull origin my_default_branch_name
```


## Remove a file from version control

Remove the file from the Git repository but not from the filesystem:

```git
$ git rm --cached file1.txt
```

If you want to remove a whole folder, you need to remove all files in it recursively. 

```git
$ git rm -r --cached folder_name
```
  
Then push changes to remote repo:

```git
$ git commit -m "Removed stuff"
$ git push origin branch_name  
```
