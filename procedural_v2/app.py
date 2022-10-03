# booststrapping code: that wraps the entire system together --> druiver/client code: it does not really need to be in OOP
from user_interface import handle_register
from logic import get_users, update_current_users_from_database
from data import write, read

# 1) get a copy from the current ussers database 

users_list_from_database = read('user.json')

# 2) no communication direct between data and logic

update_current_users_from_database(users_list_from_database)

# 3) input and register 
print(handle_register())


print("temp users in logic:")
print(get_users())

print("users list in db before write:")
print(read("user.json"))



# 4) persists changes reflected on the current users list in the logic layer into the users list in the data layer 


write(get_users())

print("users list in db after write:")
print(read("user.json"))



# print("After  commiting into database...")
# print("Current user base in the logic layer:" ,get_users(), sep="\n")
# print("Current user base in the data layer:" ,read(), sep="\n")

