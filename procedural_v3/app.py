# booststrapping code: that wraps the entire system together --> druiver/client code: it does not really need to be in OOP
from user_interface import handle_register, handle_register_inputs
from logic import get_users, update_current_users_from_database
from data import write, read, userExists
import sys




# 1) get a copy from the current ussers database 

users_list_from_database = read('user.json')

# 2) no communication direct between data and logic

update_current_users_from_database(users_list_from_database)

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




    # 4) persists changes reflected on the current users list in the logic layer into the users list in the data layer 


    write(get_users())
