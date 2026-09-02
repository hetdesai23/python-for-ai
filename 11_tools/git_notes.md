# Git & GitHub

## Version control basics
Git tracks changes to files over time so you can see history, revert
mistakes, and collaborate without overwriting each other's work.

## Core workflow
```bash
git init                       # start tracking a folder
git status                     # see what's changed
git add file.py                # stage a specific file
git add .                      # stage everything
git commit -m "Add feature"    # save a snapshot with a message
git log                        # view commit history
```

## Working with GitHub (remote repos)
```bash
git remote add origin https://github.com/username/repo.git
git branch -M main
git push -u origin main        # first push
git push                       # subsequent pushes
git pull                       # get latest changes from remote
```

## Cloning an existing repo
```bash
git clone https://github.com/username/repo.git
```

## Branching (not deep-dived in the beginner course, but good to know)
```bash
git checkout -b feature-branch
git checkout main
```

## VS Code's built-in Git
VS Code has a Source Control panel that does staging, committing, and
pushing/pulling through the UI instead of the terminal — useful while
still learning the commands.

## This repo
This exact repo was created and committed with:
```bash
git init
git add .
git commit -m "Initial commit: Python for AI course notes"
```
To publish it, create an empty repo on GitHub, then:
```bash
git remote add origin https://github.com/<your-username>/python-for-ai-course.git
git branch -M main
git push -u origin main
```
