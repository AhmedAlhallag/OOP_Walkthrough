
from data import findBy, write, read

temp_users = [] 


"""
Q: How maintain the control flow to go in one direction from outermost module --goingOneLevelDeepOnly--> to the innermost modules? 
ANS: we need to force  logic.py to be the ONLY module capable of accessing the data.py
+ we need to make the user_interface.py the ONLY module capable of accessing the logic.py
+ we need to make the app.py (client code) the ONLY module capable of accessing the user_interface.py !

BUT WHERE DO WE START? -> from logic.py

    [REFUSED SOLUTION] don't discuss this sol or why is it bad:
#  on the startup of the system (the imported file gets executed AS LONG AS IT IS NOT WITHING A if __name__ == "__main__":) 
# which is totally random and unreliable!

    [Better solution]:
1) refactor the update and make it read from the database, 
2) and call update from the logic by the handler/user_interface.py in a function called 'startup/initialize' !
"""

def update_current_users_from_database():
    global temp_users
    temp_users  = read("user.json")

"""
3) make logic overwrite the database immediatly after registering a user (that was the most logical thing to be done by the register from start!)
the call to 'write' the data into db should not have been left as a 'sequential' step for the app.py (client code) to perform from the start!
it should been invoked by the use case who's in charge! --> register! 
"""    


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
    
