import json 

import os 

cwd = os.path.dirname(os.path.realpath(__file__))

filepath = ""
def prepare_connection(filename):
    filepath = cwd + "\\" + filename
    return filepath
    
def read(filename):
    global filepath
    filepath = prepare_connection(filename)
    with open(filepath,'r') as file:
        return json.load(file) 


def write(alist):
    with open(filepath,'w') as file:
        return json.dump(alist,file)
    
    
def findBy(key, value, list):
    for d in list:
        if d[key] == value:
            return 1 
    return -1 


def UserExists(key, value, list):   
    idx = findBy(key, value, list)
    if idx != -1:
        return True
    return False


