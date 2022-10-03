# booststrapping code: that wraps the entire system together --> druiver/client code: it does not really need to be in OOP
from user_interface import handle_register, handle_register_inputs
from logic import get_users, update_current_users_from_database
from data import write, read, userExists
import sys


"""
REFACTORING DONE IN THIS VERSION (AFTER Exists check is added)
1. we need to seperate the input taking from the creation, to check the taken inputs against the db 
2. hence we changed the signature of the handle_register, and handle_resgister_inputs now is called directly from the app (conditionally)
3. we added a conditioonal to check if the user exists --> exit
4. else the registeration process continues as before 


"""

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


    # print("temp users in logic:")
    # print(get_users())

    # print("users list in db before write:")
    # print(read("user.json"))



    # 4) persists changes reflected on the current users list in the logic layer into the users list in the data layer 


    write(get_users())

    # print("users list in db after write:")
    # print(read("user.json"))



    # print("After  commiting into database...")
    # print("Current user base in the logic layer:" ,get_users(), sep="\n")
    # print("Current user base in the data layer:" ,read(), sep="\n")

