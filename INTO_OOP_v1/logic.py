
from data import findBy, write, read

temp_users = [] 

"""
Problems in the current logic.py file:

The bad:

    [Globals]
    What if i have multiple tables/JSON-FILES that need to be read/fetched?
    [PROBLEM]: we can create a global list variable for each one of these table inside the SAME logic.py
    ==> What is wrong with this suggestion? 
    
    
    
    [Create Slides to demo the naive solution] --> Logic.py will now be voilating SOC/SR principle! AND it is not cohiesive! (Doing & handling so many things)   
    ============================================== STOP ===========================================
    The next statements are related to following certain layered arch. pattern which is not the main motive of this case study
    ===============================================================================================
    
    [Initially] RULE OF THUMB FOR LOGIC CODE:
        > If I have buisness use case(s) that is dependant on certain layer of data; 
        we need to create a dedicated logic layer for these buisness use case(s)   
        
        Later on this would be structured differently once we get to know about Arch. Patterns 
    
    to what 'buisness use case' does this logic belong? --> to "Creating an account" buisness use case 
    STOP--> here we are starting to talk about ECB arch. pattern!

"""


def update_current_users_from_database():
    global temp_users
    temp_users  = read("user.json")
 


def register(un, ps):
    if userExists('un', un, temp_users):
        return False
    temp_users.append({'un':un, "ps": ps})
    # save to database
    write(get_users())
    return True
    

def userExists(key, value, alist):
    # make sure it validates any given key and value 
    idx = findBy(key, value, alist)
    if idx != -1:
        return True
    return False


def get_users():
    return temp_users 
    
