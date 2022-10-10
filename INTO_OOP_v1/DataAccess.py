"""
First Modification to be done:
    [Bad design/Naming convetion]
1. Make a copy cat of data_access.py. Name the class (on purpose) as DataAccess 
[Activity] Let the students attempt this OOP refactoring first

--> Does this feel right? 
    - for the time being we have one source of data to access (users table), what if we start to having more tables?
    - Plus, we are currently using only one type of data format (JSON), 
    what do you think would happen if we introduce some SQL tables/files? or if we completely migrated to SQL?


"""

import json

import os 
cwd = os.path.dirname(os.path.realpath(__file__))



class DataAccess:
    
    """
    Creating the constructor --> __init__():
    1. intended to 'initialize' the object to be created!
    2. Design Issue: what is the current problem in data_access.py?
    Do all function seems to abide by the SR (SOC) rule?
    Do all functions seem to be "cohesieve"?
    
    specifically, what is the current probelm with 'read()'?
    ANS: 
    - Coopled to prepare_connection!
    - It is a MUST that read is called atleast once, to setup/prepare the path of the data file we want to connect-to/open 
    - given this implementation, signatures are tightly coupled!
    - we are using globals, 
    How is this bad? it is on the module level, can be accessed and changed by "ANYONE"
    No information hiding! No abstraction! 
    [DEMO] Why are globals are bad and what are side-effects in computer science?
    - read is doing more than one thing!
        1. it prepares the connection
        2. it opens a file and reads from it!     
        
    --> removing globals: solution 2 using OOP (using instances, instance variables and maintaining a state)
    """
    
    
    def __init__(self, filename):
        """
        we pass the stored datafile path once and gets stored forever in the to-be-created object lifetime
        1. we initialize once 
        2. this data is stuck to the backgroud/pool-of-variables of this object, we can access anytime [maintaining state -> this object has state; STATEFUL]
        3. accessible ONLY by the object's methods! -> [Access control/Abstraction]
        """
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

    