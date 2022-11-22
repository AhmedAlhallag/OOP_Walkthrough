
import json

import os 
cwd = os.path.dirname(os.path.realpath(__file__))




class DataAccess:
    def __init__(self, filename):
        self.stored_datafile_path = self.prepare_connection(filename)
    
    def prepare_connection(self, filename): # config params into function that provies you with a db connection 
        stored_file_path = cwd + "\\" + filename
        return stored_file_path
    
    def read(self):
        with open(self.stored_datafile_path,'r') as afile: # INTERNAL DEPEPENDNCY ==> File
            return json.load(afile)
    
   
    def write(self,alist):
        with open(self.stored_datafile_path,'w') as afile:
            return json.dump(alist,afile)


    def findBy(self, key, value, alist):
        for i, row in enumerate(alist):
            if row[key] == value:
                return i 
        return -1
    
    
    
# Driver Code 

# da = DataAccess("fake.json")
# print(da.stored_datafile_path)

# da.read()