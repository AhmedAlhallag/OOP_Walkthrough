# booststrapping code: that wraps the entire system together --> druiver/client code: it does not really need to be in OOP
from user_interface import handle_register, handle_register_inputs
from logic import get_users, update_current_users_from_database
from data import write, read
# import sys




# 1) get a copy from the current ussers database 

users_list_from_database = read('user.json')

# 2) no communication direct between data and logic

update_current_users_from_database(users_list_from_database)

# 3) input
un, ps = handle_register_inputs()

# 4) validate use does not exist 
"""
# NOTE: if you saw condititional/loops out of no where in your script NOT IN a function --> 
# this is a premise that this is a bad design/code smell 
--> solved in logic 3.3.3
"""

"""
logic 3.3.3) cleaning the app code as much as possible:

    The Good of the current refactor:
1. No if laid out out-of-place if statments anymore! 
NOTE: if/else is not necesserily harmful; the if/elif/elif/elif... is what would be considered a source of problems!

2. The client code does not need to step a couple modules inwards and communicate with the "data.py" to some extent now!

    THE BAD:
1. The app.py (client code) is still relying on the data which is the innermost level!
2. eveything still pretty much strongly coupled to the app.py!
"""

"""
logic 3.3.4) unpack!
"""

msg, do =  handle_register(un, ps)

print(msg)
do()


# 4) persists changes reflected on the current users list in the logic layer into the users list in the data layer 


write(get_users())
