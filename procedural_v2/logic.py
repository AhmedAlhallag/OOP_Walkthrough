
temp_users = [] 

def update_current_users_from_database(alist_from_database):
    global temp_users
    temp_users  = alist_from_database
    


def register(un, ps):
    temp_users.append({'un':un, "ps": ps})

def login(un,ps):
    pass

"""
Validation logic: check account exist before sign up 
1. Validation against fields of DB --> in entity
2. Validation against buisness use case logic  --> in control/service
"""

def is_valid():
    return True # or False 
    

def get_users():
    return temp_users 
    
