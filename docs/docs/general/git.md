# Git Version Control System

### Starting repositories 

Clone an existing repository: `$ git clone ssh://user@domain.com/repo.git` 

Create a new local repository: `$ git init`


### Local changes

Show changed files in your working directory: `$ git status`

Add all current changes to the next commit: `$ git add`

Add some changes in <file> to the next commit: `$ git add -p <file>`

Commit all local changes in tracked files: `$ git commit -a`


### Remove a file from version control
Remove the file from the Git repository and from the filesystem

```git
git rm file1.txt
git commit -m "remove file1.txt"
```
But if you want to remove the file only from the Git repository and not remove it from the filesystem, use:
```git
git rm --cached file1.txt
git commit -m "remove file1.txt"
```
Then push changes to remote repo
```
git push origin branch_name  
```
