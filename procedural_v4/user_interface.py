# take inputs from the end user/ client 
from logic import register, update_current_users_from_database
import sys
# name this file as handler.py 

def initialize():
    update_current_users_from_database()
    print("[DATA IMPORTED] System initialzed!")
    

def handle_register_inputs():
    un = input("Enter your un: ")
    ps  = input("Enter your ps: ")
    return un, ps



def handle_register(un, ps):
    if register(un, ps):
        return "Your account has been created", print
    return "[ERROR] An account with this name already exists.", sys.exit



    
    
    
     
    




