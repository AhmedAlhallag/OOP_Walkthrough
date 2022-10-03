import json
# users_in_database = [{'un':'haidy',"ps":123}]

import os 
# print(os.path.dirname(os.path.realpath(__file__)))
cwd = os.path.dirname(os.path.realpath(__file__))


"""
Design decision:
- either stored_file_path is a global
- or to be returned and the return is either passed to read
- or the read it self is calling the prepare_connection but for that you will be sending the argument the prepare_connection need via the read function
"""

"""
We can make stored_file_path global for the sake of NOT letting the logic layer instantiate the connection to the file/table(DB)
the DAO is the layer responsible for connecting to files/tables
AND keeping a live copy of the rows/data 
"""

"""
BAD DEISGN: Instead of instantiating the connection each time before performing any of the CRUD operations
Notice how even the write function now needs a the filename to execute the write operation 
"""
def prepare_connection(filename):
    stored_file_path = cwd + "\\" + filename
    return stored_file_path
 
def read(filename):
    stored_file_path =  prepare_connection(filename)
    with open(stored_file_path,'r') as afile:
        return json.load(afile)

def write(alist, filename):
    stored_file_path =  prepare_connection(filename)
    with open(stored_file_path,'r') as afile:
        return json.load(afile)


    


# print(prepare_connection('users.json'))
    
"""
print(os.path.realpath(__file__))
returns the 'file' path 
D:\2022\OOP_Motiv\procedural_v2\data.py

we want the parent directory that this file (data.py) which is opening the json file from the inside 
D:\2022\OOP_Motiv\procedural_v2\
"""

"""
print(os.path.dirname(os.path.realpath(__file__)))
This is will return the relative directory path of the file that opens (data.py or essentially any file) the json file (in this case users.json)
"""
# with open('user.json','r') as afile:
#     print(json.load(afile))

