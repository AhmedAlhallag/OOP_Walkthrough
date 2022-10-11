"""
Discussions/brainstorming:

--> Does this feel right? 
    - for the time being we have one source of data to access (users table), what if we start to having more tables?
    - Plus, we are currently using only one type of data format (JSON), 
    what do you think would happen if we introduce some SQL tables/files? or if we completely migrated to SQL?
    - The class of dataaccess seems "generic" which means it can be used to access any file given by its filename
    what do you think of this? 

"""

import json

import os 
cwd = os.path.dirname(os.path.realpath(__file__))



class DataAccess:
    def __init__(self, filename):
        self.stored_datafile_path = self.prepare_connection(filename)
    
    def prepare_connection(self, filename):
        """
        [Activity]: 
        """
        stored_file_path = cwd + "\\" + filename
        return stored_file_path
    
    def read(self):
        """
        SR/Cohisive function: doing one thing
        """
        with open(self.stored_datafile_path,'r') as afile:
            return json.load(afile)
    
    """
        [BAD DESIGN]'
        do you think that there is something off with "alist" arg that we are passing to write and findBy, EVERYTIME we call them?
        Is there a better refactor? what can we do to fully utilize the classes/instances concept?
    """
    
    def write(self,alist):
        with open(self.stored_datafile_path,'w') as afile:
            return json.dump(alist,afile)


    def findBy(self, key, value, alist):
        for i, row in enumerate(alist):
            if row[key] == value:
                return i 
        return -1

    