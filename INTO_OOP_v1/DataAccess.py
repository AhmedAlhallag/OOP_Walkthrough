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
    """
    pass
    

    