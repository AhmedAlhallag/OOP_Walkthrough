import json
# users_in_database = [{'un':'haidy',"ps":123}]

import os 
# print(os.path.dirname(os.path.realpath(__file__)))
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



    



# How can we improve this to search for any column?
def findByUn(un, alist):
    # Note: kda kda the list will be fetched by a SELECT * FROM  <TABLE>
    # so in procedural: either pass iit to arg
    # or READ it wtithing the arg --> i think this would be the solution to go for 
    # or access it from a global var 
    # in OOP -->  an instance variable does the trick
    for i, row in enumerate(alist):
        if row['un'] == un:
            return i 
    return -1
"""
a more versatile/dynamic version: give both the key and the value
"""

def findBy(key, value, alist):
    for i, row in enumerate(alist):
        if row[key] == value:
            return i 
    return -1

# put this in logic
# def userExists(key, value, alist):
#     # make sure it validates any given key and value 
# idx = findBy(key, value, alist)
# if idx != -1:
#     return True
# return False

