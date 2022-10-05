import json

import os 
cwd = os.path.dirname(os.path.realpath(__file__))



stored_file_path = ""

def prepare_connection(filename):
    stored_file_path = cwd + "\\" + filename
    return stored_file_path
 
def read(filename):
    global stored_file_path 
    stored_file_path = prepare_connection(filename)
    with open(stored_file_path,'r') as afile:
        return json.load(afile)

def write(alist):
    with open(stored_file_path,'w') as afile:
        return json.dump(alist,afile)


def findBy(key, value, alist):
    for i, row in enumerate(alist):
        if row[key] == value:
            return i 
    return -1

