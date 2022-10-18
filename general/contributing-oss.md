# Guide to contributing on GitHub

## 1) Fork the project repository

Forking the repository creates a copy of the project repository in your GitHub account.

## 2) Clone your fork

Clone or download the repository to your local machine.

Alternetively, using Git on your local machine, you can clone your fork using its URL: 

```
git clone URL_OF_FORK.
```

## 3) Check that your fork is the "origin" remote

You are going to be synchronizing your local repository with both the project repository (on GitHub) and your fork (also on GitHub). The URLs that point to these repositories are called "remotes". More specifically, the project repository is called the "upstream" remote, and your fork is called the "origin" remote.

When you cloned your fork, that should have automatically set your fork as the "origin" remote. Use `git remote -v` to show your current remotes. You should see the URL of your fork next to the word "origin".

If you don't see an "origin" remote, you can add it using: 

```
git remote add origin URL_OF_FORK.
```

## 4) Add the project repository as the "upstream" remote

Add the project repository as the "upstream" remote using: 

```
git remote add upstream URL_OF_PROJECT
```

Use `git remote -v` to check that you now have two remotes: an origin that points to your fork, and an upstream that points to the project repository.

## 5) Pull the latest changes from upstream into your local repository

Before you start making any changes to your local files, it's a good practice to first synchronize your local repository with the project repository. Use `git pull upstream master` to "pull" any changes from the "master" branch of the "upstream" into your local repository. (If the project repository uses "main" instead of "master" for its default branch, then you would use `git pull upstream main` instead.)

If you forked and cloned the project repository just a few minutes ago, it's very unlikely there will be any changes, in which case Git will report that your local repository is "already up to date". But if there are any changes, they will automatically be merged into your local repository.


## 6) Create a new branch

Rather than making changes to the project's "master" branch, it's a good practice to instead create your own branch. This creates an environment for your work that is isolated from the master branch.

Use `git checkout -b BRANCH_NAME` to create a new branch and then immediately switch to it. The name of the branch should briefly describe what you are working on, and should not contain any spaces.

Use `git branch` to show your local branches. You should see your new branch as well as "master", and your new branch should have an asterisk next to it to indicate that it's "checked out" (meaning that you're working in it).


## 7) Make changes in your local repository

Use a text editor or IDE to make the changes you planned to the files in your local repository. Because you checked out a branch in the previous step, any edits you make will only affect that branch.


## 8) Commit your changes

After you make a set of changes, use `git add -A` to stage your changes and `git commit -m "DESCRIPTION OF CHANGES"` to commit them.

If you are making multiple sets of changes, it's a good practice to make a commit after each set.


## 9) Push your changes to your fork

When you are done making all of your changes, upload these changes to your fork using `git push origin BRANCH_NAME`. This "pushes" your changes to the "BRANCH_NAME" branch of the "origin" (which is your fork on GitHub).


## 10) Begin the pull request

Return to your fork on GitHub, and refresh the page. You may see a highlighted area that displays your recently pushed branch.

Click the green Compare & pull request button to begin the pull request.

## 11) Create the pull request

When opening a "pull request", you are making a "request" that the project repository "pull" changes from your fork. You will see that the project repository is listed as the "base repository", and your fork is listed as the "head repository".

Before submitting the pull request, you first need to describe the changes you made (rather than asking the project maintainers to figure them out on their own). You should write a descriptive title for your pull request, and then include more details in the body of the pull request. If there are any related GitHub issues, make sure to mention those by number.

Below the pull request form, you will see a list of the commits you made in your branch, as well as the "diffs" for all of the files you changed.

If everything looks good, click the green Create pull request button!

## 12) Review the pull request

You have now created a pull request, which is stored in the project's repository (not in your fork of the repository). It's a good idea to read through what you wrote, as well as clicking on the Commits tab and the Files changed tab to review the contents of your pull request.

If you realize that you left out some important details, you can click the 3 dots in the upper right corner to edit your pull request description.

## 13) Add more commits to your pull request

You can continue to add more commits to your pull request even after opening it! For example, the project maintainers may ask you to make some changes, or you may just think of a change that you forgot to include.

Start by returning to your local repository, and use `git branch` to see which branch is currently checked out. If you are currently in the master branch (rather than the branch you created), then use `git checkout BRANCH_NAME` to switch.

Then, you should repeat steps 7 through 9: make changes, commit them, and push them to your fork.

Finally, return to your open pull request on GitHub and refresh the page. You will see that your new commits have automatically been added to the pull request.

## 14) Discuss the pull request

There may be questions or discussion about your pull request from the project maintainers.

Click the Resolve conversation button once you have addressed any specific requests.


## 15) Delete your branch from your fork

If the project maintainers accept your pull request, they will merge your proposed changes into the project's master branch and close your pull request. You will be given the option to delete your branch from your fork, since it's no longer of any use.


## 16) Delete your branch from your local repository

You should also delete the branch you created from your local repository, so that you don't accidentally start working in it the next time you want to make a contribution to this project.

First, switch to the master branch: `git checkout master`.

Then, delete the branch you created: `git branch -D BRANCH_NAME`. 


## 17) Synchronize your fork with the project repository

At this point, your fork is out of sync with the project repository's master branch.

To get it back in sync, you should first use Git to pull the latest changes from "upstream" (the project repository) into your local repository: `git pull upstream master`.

Then, push those changes from your local repository to the "origin" (your fork): `git push origin master`.

If you return to your fork on GitHub, you will see that the master branch is "even" with the project repository's master branch.


## References

- [Step-by-step guide to contributing on GitHub by Data School](https://www.dataschool.io/how-to-contribute-on-github/)
