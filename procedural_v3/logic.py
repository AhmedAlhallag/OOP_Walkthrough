
# needed (a dependency) by userExists 
from data import findBy
# import sys

temp_users = [] 

def update_current_users_from_database(alist_from_database):
    global temp_users
    temp_users  = alist_from_database
    

"""
# logic.2) since this validation is related to the registr, now we can use it within it 
# TWO options here to call userExists within register

A. redefine the signature of register --> register(un, ps, alist)
and hence you will modify it wherever its called in whichever script --> CODE SMELL: NO REBUSTNESS

B. To declare the temp_users as a global variable within the register function and pass it to userExists 
HENCE we would not be changing the signature of userExists nor findBy nor register!
psst: globals are still not favorable in programming, we will see how OOP reduces them

"""

"""
logic.3.1) the incorrect way: placing the thrown excpetion/errror messages IN THE SAME FUNCTION THAT DOES THE VALIDATION LOGIC; 
processing logic + displaying output....voilating SR much?

"""


def register_Voilates_SR(un, ps):
    # global temp_users
    # Note: accessing/reading globals from functions does not require them to be declared within functions; 
    # only re-assignment does (total change to the global)
    if userExists('un', un, temp_users):
        print('[ERROR] An account with this name already exists.')
        # sys.exit()
    else:
        temp_users.append({'un':un, "ps": ps})

"""
#logic.3.2.2) 
"""

def register(un, ps):
    if userExists('un', un, temp_users):
        return False
    temp_users.append({'un':un, "ps": ps})
    return True
    


"""
# logic.1) this will need an import for the data access; start of communication between logic <-> data  
"""
def userExists(key, value, alist):
    # make sure it validates any given key and value 
    idx = findBy(key, value, alist)
    if idx != -1:
        return True
    return False


def get_users():
    return temp_users 
    
