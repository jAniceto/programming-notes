Title: Git Version Control System
Date: 2017-09-11 10:41
Authors: José Aniceto
Modified: 2018-08-30 13:55

## Instalation on a Debian-based distribution, such as Ubuntu

```
$ sudo apt update
$ sudo apt install git-all
```

### Starting repositories 

Clone an existing repository: `$ git clone ssh://user@domain.com/repo.git` 

Create a new local repository: `$ git init`


### Local changes

Show changed files in your working directory: `$ git status`

Add all current changes to the next commit: `$ git add`

Add some changes in <file> to the next commit: `$ git add -p <file>`

Commit all local changes in tracked files: `$ git commit -a -m "Changed something"`


### Working with remote repository

Grab changes from remote: `$ git pull origin master`

If your default branch is different than master, you will need to specify the branch name: `git pull origin my_default_branch_name`

Upload changes to remote: `$ git push origin master`


### Remove a file from version control
Remove the file from the Git repository and from the filesystem

```git
$ git rm file1.txt
$ git commit -m "remove file1.txt"
```
But if you want to remove the file only from the Git repository and not remove it from the filesystem, use:
```git
$ git rm --cached file1.txt
$ git commit -m "remove file1.txt"
```
Then push changes to remote repo
```
$ git push origin branch_name  
```
