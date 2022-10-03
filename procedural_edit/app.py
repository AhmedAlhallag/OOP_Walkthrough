# booststrapping code: that wraps the entire system together --> druiver/client code: it does not really need to be in OOP
from user_interface import handle_register
from logic import get_users, update_current_users_from_database
from data import write, read

# 1) get a copy from the current ussers database 

users_list_from_database = read()

print("Before updating..")
print("id of temp_users_list_in_logic_layer", id(get_users()), end='\n\n')
print("id of users_list_in_Db", id(users_list_from_database), end='\n\n')
# 2) no communication direct between data and logic
# so we need to make sure that the users list in logic is up to date with the current database of users from the data.py

print("After updating..")
update_current_users_from_database(users_list_from_database)
print("id of temp_users_list_in_logic_layer", id(get_users()), end='\n\n')
print("id of users_list_in_Db", id(users_list_from_database), end='\n\n')

# 3) input and register 
print(handle_register())

# 4) persists changes reflected on the current users list in the logic layer into the users list in the data layer 

print("Before  commiting into database...")
print("Current user base in the logic layer:" ,get_users(), sep="\n")
print("Current user base in the data layer:" ,read(), sep="\n")
print("\n")


write(get_users())




print("After  commiting into database...")
print("Current user base in the logic layer:" ,get_users(), sep="\n")
print("Current user base in the data layer:" ,read(), sep="\n")

