# Git
Will let us keep track of changes. Git will let us save "snapshots".
On larger webapplications, one trick part of the process is that many people work in the server at the same time.

Git allows us to try to test the changes in our codes without the need to substitute with the original. We do that by separating in different branchs.

We also have an ability to reserve to previous versions of the code.

The code must be hosted in a server.

# Github
## git clone
Download a repository from the internet into your machine.
The download can be done in HTTPS or in SSH. Both are methods of authentication.
```
git clone {url}
```
`ls` or `dir`: shows all the files inside a directory.
`cd`: change directory.
`touch`: create a new file.

```
touch hello.html
```

`code .`: will open a VS studio project with that directory.

## git commit
Save the current state of the git repository.
To do that, we need somethings before...
1. git add: add files to the commit. The git commit can de done individually or to all files `add .`.
2. git status: to see what is changed and what is not.

git commmit -am: combine the steps of add and commit with `commit -am "Add this file"`. In this way, we have added all files and commited them.

## git push
To push changes to github.

## git pull
In case the github version is more recent than our own. We use the command git pull. The git pull command will take the version in github to our machine. It is exactly the opposite of git push.

# Merge Conflicts
When both do changes in some file, we end up in a merge conflict.

A common message in that is:
```
CONFLICT (content): Merge conflict in foo.py
Automatic merge failed; fix conflicts and then
commit the result.
```

The git will automatically add a meta file to show what is conflicting:

```
a = 1
<<<<< HEAD
b = 2
=====
b = 0
>>>>> 5791372102731dedq17210d7ed221
```
Before the equal signs we have our local changes.
After the equal signs we have the remote changes.

What we see as well we get a hash to identify the commit.

Therefore, to solve he conflict, we must erase those extra lines and define which version we want to keep.

The VS Code IDE already gives the possible options.

After resolving, you need to erase the markers.

## git log
Show all the commits that were made and what happened.

## git reset
If a previous version is better than a current one, `git reset` can be used to go back to a previous version of the code.

Going back to a specific commit:
```
git reset --hard <commit hash> # the hash can be viewed in log
```

Or going back to a specific branch:

```
git reset --hard origin/master
```

# Branching
When we start working on a new feature, the best idea is to create a new branch.

The branch helps us to work in different parts of the repository at the same time.

The `master` branch will have the up to date stable application version.

New additional features can be created on other branchs.

## HEAD 
The head points to where we are working right now.

After we have finished working in a branch, we can merge it to the master branch.

## git branch
Will show in which branch we are.

## git checkout -b {new_branch}
When we want to switch to a branch does not yet exist.
```
Switched to a new branch '{new_branch}'
```

add new line