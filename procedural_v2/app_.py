from user_interface import handle_register_inputs, handle_register
from logic import update_current_users_from_database, get_users
from data_ import read, write, UserExists
import sys

# 1) read the current user list from db 

users_list_from_database = read('user.json')


# 2) Uplaod/Sync the fetched user from database with the temp users list inside th logic.py

update_current_users_from_database(users_list_from_database)

# --> 


un, ps = handle_register_inputs()

if UserExists('un', un, get_users()):
    print("Account exists sorry")
    sys.exit()
else:

    # 3) perform the register
    print(handle_register(un, ps))


    # 3 save to db
    write(get_users())
    
    
