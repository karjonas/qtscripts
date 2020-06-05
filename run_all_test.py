#!/usr/bin/python
import subprocess
import os.path

files = subprocess.check_output(["find", ".", "-iname", "tst_*.cpp"]).decode("utf-8").split('\n')
files = sorted(list(filter(lambda x: x != None and "/auto/" in x, files)))

print(__file__ + ": Found " + str(len(files)) + " autotest files", flush=True)

for file in files:
    file_raw_a = file.replace('.cpp','')
    file_raw_b = file_raw_a.replace('tst_', '')
    return_code = 0

    if os.path.isfile(file_raw_a):
        return_code = subprocess.call(file_raw_a)
    elif os.path.isfile(file_raw_b):
        return_code = subprocess.call(file_raw_b)
    else:
        print(__file__ + ': Could not find file for ' + file, flush=True)
    print(__file__ + ': ' + file + ' returned ' + str(return_code), flush=True)
    
