
temp_users = [] 

def update_current_users_from_database(alist_from_database):
    global temp_users
    temp_users  = alist_from_database
    


def register(un, ps):
    temp_users.append({'un':un, "ps": ps})




def get_users():
    return temp_users 
    
