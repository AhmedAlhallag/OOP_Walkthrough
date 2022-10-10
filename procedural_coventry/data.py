""" This is to access and query the data stored in a list (with a dictionary for each
user"""
# empty list of users
users = []
def read_users():
    return users
def write_users(list):
    users = list
    
    
import json

open('procedural_coventry\\test.json','r')

# we need to reach the relevant parent folder in which the test.json is in IN CASE WE RUN IT FROM ANYWHERE :

import  os 


path_of_file = os.path.realpath(__file__)
print(path_of_file)  
path_of_relevant_parent_folder = os.path.dirname(os.path.realpath(__file__))
print(path_of_relevant_parent_folder)  

filename = "test.json"
dynamic_file_path = path_of_relevant_parent_folder + "\\" + filename 

print(dynamic_file_path)
open(dynamic_file_path,'r')



