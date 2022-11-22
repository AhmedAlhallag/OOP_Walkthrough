

"""
What's BAD about this code:

    data.py

1. prepare_connection is invoked every time the read function is executed (read is voilating the DRY principle)
2. every time the read function is excuted, a global variables is access and re-assigned (globals are the cause of high coupling)
3. read is highly coupled to prepare_connection, solution? [procedural] by dependdency injection/association; sending the stored_file_path as an argument
BUT IF WE DID THIS;
- We would be exposing the driver code to ALOT of data acess logic (weak 'information hiding'),
a better choice would be to expose the leaast number possible of functions of the data access (i.e.: read -> calls implicitly prepare_connection) 
4. for the Write function, the read MUST atleast run once (depeendency -> high coupling) 
5. No single responsipility; data.py is not cohesive; UserExist is a validation logic that is only related to the user table/json file, suggested solution? put it in logic.py?  
6. every time we need to perform a 'search/findBy' or an "existance check" we need to pass the current users list as an argument
How easy would it have been if we had that list stored in some sore of state (aka: "object"!)

    logic.py
     
1. logic is trying as best as it can to maintain a 'state' of the current user list; 
while capturing the initial state from the db at the start of the program AND updating the db with the new state by the end of the registration use case
2. Maintaining state is poorly implemented by depending on 'globals'
3. register function is not robust (voilating Open/Closed Principle --> 'O' from SOLID, what happens if we need to take email? ps2? phone_number?
--> How many things will break? How many things need to be changed?  Solution: DTOs


    user_interface.py

1. handle_register and handle_register_inputs were highly coupled before refactoring (commit: adding Userexits)

    Control Flow
    
The current flow is 'naive' --> depending heavily on the driver code (app.py); the (dependency) control flow between modules is almost zero
; What if app.py got deleted? --> no system!



=================================================================================
What's GOOD about this code:

    user_interface.py
    
1. (loose coupling) we segregated the input gathering logic from the creation logic (commit where we added exists and refactored handle_register and handle_register_inputs)
2. we seperated the validation (database related --> data access layer) logic from the creation logic (buisness use case --> buisness logic) 
2.1 UPDATE: database related validations (field level validations should be done the DB level; via DBMS or via models if the framework is using ORM)
AND: the userExists validation is related to a core buisness logic --> register! so it should be IN the logic file!
--> validations related to anything else rather than db level fields should be in Service layer (BLL) 
;BUT thrown error messages/exepction can be called in the controller, the one who invoke the validation checks from the service layer
;Controller essentially should work as translator/mediator between routes and (rendered or serialized) responses
;AND they should be as thing as possible (abiding by the MVC)
--> field level validations --> DB level or Model (ORM) level [not refering to the entity or POJOs in the second one]
--> DAO should be simple related to only fetching from db and storing into db 
--> some would say the search/findBy would even be suited in Service layer BLL


"""












"""
Design decision:
- either stored_file_path is a global
- or to be returned and the return  is either passed to read
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

INSTEAD: 
we can make the prepare_connnection (+ assign the stored_file_path the file path once) happen once;
probably when the first read operation takes place 
+ make the stored_file_path a global variable that can be accessed by read or write whenever they need
"""
import json
import os 
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




"""
Note regarding account_is_valid [existance check validation logic]
when we have a DAO for the user table, we should put the account_is_valid in it
As long as we don have a dedicated DAO, we can have it in the buisness logic 
(1. wrong because not a buisness use case, and 2. if it were to be a class, it would probably be a static method)

3. Not to mention that this is a validation against the DB, so it should be in DAO

UPDATE: lets put it in DAO (data.py)
========================================
2.1 UPDATE: database related validations (field level validations should be done the DB level; via DBMS or via models if the framework is using ORM)
AND: the userExists validation is related to a core buisness logic --> register! so it should be IN the logic file!
(even if it was a validation against the DB; it is still concerning a buisness use case)

--> validations related to anything else rather than db level fields should be in Service layer (BLL) 
;BUT thrown error messages/exepction can be called in the controller, the one who invoke the validation checks from the service layer
;Controller essentially should work as translator/mediator between routes and (rendered or serialized) responses
;AND they should be as thing as possible (abiding by the MVC)
--> field level validations --> DB level or Model (ORM) level [not refering to the entity or POJOs in the second one]
--> DAO should be simple related to only fetching from db and storing into db 
--> some would say the search/findBy would even be suited in Service layer BLL

============================= this edit can be found in v3 (intro to linking data with logic)


"""
def userExists(key, value, alist):
    # make sure it validates any given key and value 
    idx = findBy(key, value, alist)
    if idx != -1:
        return True
    return False

    


"""
I think findBy or search should be in the Buisnesss logic layer --> WRONG it should be in the data layer 
UNLESS the search (usually by a certain critera) is a buisenss use case
"""

"""
NOTE: you would not need to specify a table as an  argument to the findByUn function (or any CRUD)
since idealy,  you would a DAO for each table, so the table can be either set via the constructor, or via a connection function
"""

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

