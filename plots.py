#!/usr/bin/python3
import json
import sys
import os

def parse(argv):
   if len(argv) == 1:
       print('invalid number of arguments')
       print('Expecting ' + argv[0] + ' file_a file_b ... file_n')
       sys.exit(1)
   return argv[1:]

def load_json(input_file):
    with open(input_file) as f:
      data = json.load(f)
      return data
    return {}

def commonprefix(json_files):
    keys = []
    for json_data in json_files:
        for key, _value in json_data.items():
            if not ignore_key(key):
                keys += [key]
    return os.path.commonprefix(keys)

def ignore_key(key):
    ignore_keys = ['command-line', 'id', 'opengl', 'os', 'qt', 'windowSize']
    return key in ignore_keys

def get_keys(json_files):
    keys = []
    for json_data in json_files:
        for key, _value in json_data.items():
            if not ignore_key(key):
                keys += [key]
    return list(dict.fromkeys(keys))

def has_key(json_data, key):
    for k, _value in json_data.items():
        if k == key:
            return True
    return False

def main(argv):
    files = parse(argv)
    #print(files)
    json_files = []
    for file in files:
        json_files += [load_json(file)]
    json_ids = []
    for file in json_files:
        json_ids += [file['id']]
    #print(json_ids)
    #print(json_files)
    common_prefix = commonprefix(json_files)
    #print(common_prefix)
    print('test_name, ' + ', '.join(json_ids))

    for key in get_keys(json_files):
        test_frames = []
        key_clean = key.replace(common_prefix, '')
    
        for json_data in json_files:
            if not has_key(json_data, key):
                print('Missing key ' + key + ' in ' + json_data['id'], file=sys.stderr)
                test_frames += ["-1"]
                continue
            test_frames += [str(json_data[key]['average'])]
        print(key_clean + ', ' +  ', '.join(test_frames))
        
if __name__ == "__main__":
   main(sys.argv)