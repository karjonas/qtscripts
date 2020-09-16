#!/usr/bin/python

# To install pyyaml: pip install pyyaml
import subprocess
import os.path
import os
import yaml

cwd = os.getcwd()
folders = [(cwd, None)]
visited = []

while folders:
    (dir,sha) = folders[0]
    folders = folders[1:] # pop first

    if sha in visited:
        continue
    visited = visited + [sha] # add new sha

    print("\nAt " + dir)

    # Verify commit is new enough
    if not sha == None:
        subprocess.check_output(["git", "remote", "update", "origin"], cwd=dir)
        curr_sha = subprocess.check_output(["git", "rev-parse", "--verify", "HEAD"], cwd=dir).decode("utf-8").strip()
        curr_msg = subprocess.check_output(["git", "show", "-s", "--format=%s", curr_sha], cwd=dir).decode("utf-8").strip()
        need_msg = subprocess.check_output(["git", "show", "-s", "--format=%s", sha], cwd=dir).decode("utf-8").strip()

        print('At ' + curr_sha + ', ' + curr_msg)
        print('Needs ' + sha + ', ' + need_msg)
        is_ok = subprocess.call(["git", "merge-base", "--is-ancestor", curr_sha, sha], cwd=dir) == 0
        if is_ok:
            print('Satisfied')
        else:
            print('Not satisfied, checking out...')
            subprocess.call(["git", "remote", "update", "origin"], cwd=dir)
            subprocess.call(["git", "checkout", sha], cwd=dir)

    file_path = dir + "/dependencies.yaml"

    if not os.path.isfile(file_path):
        print("Could not find " + file_path)
        abort()

    print("Opening " + file_path)
    file_data = open(file_path, "r").read()
    my_yaml = yaml.load(file_data,  Loader=yaml.BaseLoader)

    for k, v in my_yaml['dependencies'].items():
        folder = os.path.normpath(dir + "/" + k)
        sha = my_yaml['dependencies'][k]['ref']
        print('Adding dependency ' + folder + ', ' + sha)
        folders = folders + [(folder, sha)]
        
    