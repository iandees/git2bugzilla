#!/bin/python

import sys

import git
import re

repo_path = sys.argv[1]



# Fetch from the remote
g = git.Git(repo_path)
g.fetch()

# Look for commits between master and origin/master
repo = git.Repo(repo_path)
for commit in repo.commits_between('master', 'origin/master'):
    match = re.search(regex, commit.message)


# After completion fast-forward to origin/master
g.rebase('origin/master')
