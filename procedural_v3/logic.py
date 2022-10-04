
from data import findBy


temp_users = [] 

def update_current_users_from_database(alist_from_database):
    global temp_users
    temp_users  = alist_from_database
    


def register(un, ps):
    temp_users.append({'un':un, "ps": ps})



# this will need an import for the data access; start of communication between logic <-> data  
def userExists(key, value, alist):
    # make sure it validates any given key and value 
    idx = findBy(key, value, alist)
    if idx != -1:
        return True
    return False


def get_users():
    return temp_users 
    
