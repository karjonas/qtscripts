#!/usr/bin/python
import subprocess

# Get repo name
origin_address = subprocess.check_output(["git", "remote", "get-url", "origin"]).decode("utf-8").strip()
repo_name = origin_address.split("/")[-1].split(".")[0]
gerrit_name = "ssh://jokarlss@codereview.qt-project.org:29418/qt/"+repo_name
print("Found repo name " + repo_name)

# add gerrit remote
print("Removing gerrit remote")
subprocess.check_output(["git", "remote", "remove", "gerrit"])
print("Adding remote " + gerrit_name)
subprocess.check_output(["git", "remote", "add", "gerrit", "ssh://jokarlss@codereview.qt-project.org:29418/qt/"+repo_name])