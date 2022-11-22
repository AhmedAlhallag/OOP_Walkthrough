
temp_users = [] # Contains nothing now!!

def update_current_users_from_database(alist_from_database):
    global temp_users
    temp_users  = alist_from_database
    


def register(un, ps):
    temp_users.append({'un':un, "ps": ps})


"""
Validation logic: check account exist before sign up 
1. Validation against fields of DB (like the one in this case) --> in entity/DAO
2. Validation against buisness use case logic  --> in control/service
WRONG
Check the edit/note on this data.py from v2
"""


    

def get_users():
    return temp_users 
    

# print("running from logic.py...")