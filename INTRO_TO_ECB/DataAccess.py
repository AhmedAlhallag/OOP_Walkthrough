
import json

import os 
cwd = os.path.dirname(os.path.realpath(__file__))




class DataAccess:
    def __init__(self, filename):
        self.stored_datafile_path = self.prepare_connection(filename)
    
    def prepare_connection(self, filename): 
        stored_file_path = cwd + "\\" + filename
        return stored_file_path
    
    def read(self):
        with open(self.stored_datafile_path,'r') as afile: 
            return json.load(afile)
    
   
    def write(self,alist):
        with open(self.stored_datafile_path,'w') as afile:
            return json.dump(alist,afile)

    """
    First problem encountered once we find more than a "single" domain object..
    Now that there are blogs, this search function defition would not cut it
    we need to grab ALL blogs, not just the first match! 
    """
    def findBy(self, key, value, alist):
        for i, row in enumerate(alist):
            if row[key] == value:
                return i 
        return -1
    
    """
    To accomodate:
    """
    def findAllBlogsOfUser(self):
        pass 
    """
    One good note: 
    - Put all searching functions as "business use cases" in your business layer, rather than in the DataAccess Layer
    because eventually it will be very specific ..
    """