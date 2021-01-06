#!/usr/bin/python
import subprocess

# Get repo name
origin_address = subprocess.check_output(["git", "remote", "get-url", "origin"]).decode("utf-8").strip()
repo_name = origin_address.split("/")[-1].split(".")[0]
gerrit_name = "ssh://jokarlss@codereview.qt-project.org:29418/qt/"+repo_name
print("Found repo name " + repo_name)

# add gerrit remote
print("Trying to remove gerrit remote")
subprocess.call(['git', 'remote', 'remove', 'gerrit'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
print("Adding remote " + gerrit_name)
subprocess.check_output(["git", "remote", "add", "gerrit", "ssh://jokarlss@codereview.qt-project.org:29418/qt/"+repo_name])
