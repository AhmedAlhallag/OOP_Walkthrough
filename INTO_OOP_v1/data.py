import json

import os 
cwd = os.path.dirname(os.path.realpath(__file__))



stored_file_path = ""

def prepare_connection(filename):
    stored_file_path = cwd + "\\" + filename
    return stored_file_path
 
def read(filename):
    global stored_file_path 
    print("testing global is changed:", stored_file_path )
    stored_file_path = prepare_connection(filename)
    with open(stored_file_path,'r') as afile:
        return json.load(afile)
    
"""
[Activity] A suggested solution to minimize globals using returns:
TODO: Come up with a solution that eliminates the need to use globals!

"""

def write(alist):
    with open(stored_file_path,'w') as afile:
        return json.dump(alist,afile)


def findBy(key, value, alist):
    for i, row in enumerate(alist):
        if row[key] == value:
            return i 
    return -1

"""
Solutions:

1. (v2) Either that both write and read implicitly call prepare connection within the function (v2)
This solution has been dicussed before; 

PROS: 
No globals 

CONS:
it introduce redudencay (voilates DRY) and more coupling (to prepare_connection and to signatures of outer and inner level functions)

"""
def read_v2(filename):
    stored_file_path = prepare_connection(filename)
    with open(stored_file_path,'r') as afile:
        return json.load(afile)

def write_v2(alist, filename):
    stored_file_path = prepare_connection(filename)
    with open(stored_file_path,'w') as afile:
        return json.dump(alist,afile)

"""
OR (v3)
2. rely on the client (the script that will use these functions; it can be app.py, logic.py, etc..) in:
    A) calling prepare function first
    B) passing the returned value to read
    C) and to write
    
PROS:
This way we removed coupling at all, BUT

CONS:
- we need to rely on the client to prepare the connection (poor abstraction)
WE ARE ADDING MORE COMPLEXITY TO THE CONSUMER OF THIS FUNCTION

PLUS: A service/module/class needs to be fully packaged! providing minimal interfaces to the user/client script to use
+ Abstraction actually means: reducign complexity by hiding unnecessary details 
(like the call to prepare_connections; can't this just be ran behind the scenes? as a develoepr i can forget to call it no?) 

- EVERY TIME we want to perform a CRUD operation, we need to pass the path/to/data/file to read and write functions! (voilates DRY)

"""

def read_v3(path_to_data_file):
    with open(path_to_data_file,'r') as afile:
        return json.load(afile)

def write_v3(alist, path_to_data_file):
    with open(path_to_data_file,'w') as afile:
        return json.dump(alist,afile)
