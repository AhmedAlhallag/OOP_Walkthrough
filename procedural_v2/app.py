# booststrapping code: that wraps the entire system together --> druiver/client code: it does not really need to be in OOP
from user_interface import handle_register, handle_register_inputs
from logic import get_users, update_current_users_from_database
from data import write, read, userExists

import logic

import sys



# 1) get a copy from the current ussers database 

users_list_from_database = read('user.json')

# 2) no communication direct between data and logic

update_current_users_from_database(users_list_from_database)

print(get_users())

# Side effects --> module level variables 

# logic.temp_users = "Contains nothing now!!"

print(get_users())

# 3) input
un, ps = handle_register_inputs()

# 4) validate use does not exist 

print(get_users())
if userExists('un', un, get_users()):
    print('An account with this name already exists.')
    sys.exit()
else:

    # 5) register 
    print(handle_register(un, ps))


    write(get_users())
