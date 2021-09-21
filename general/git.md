# Git Version Control System

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
Remove the file from the Git repository but not from the filesystem

```git
$ git rm --cached file1.txt
```

If you want to remove a whole folder, you need to remove all files in it recursively. 

```git
$ git rm -r --cached folder_name
```
  
  
Then push changes to remote repo
```
$ git commit -m "Removed stuff"
$ git push origin branch_name  
```
