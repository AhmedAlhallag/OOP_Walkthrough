# take inputs from the end user/ client 
from logic import register, update_current_users_from_database
import sys
# name this file as handler.py 

"""
    [BAD DESIGN]

User_interface is doing something that voilates SOC
It is doing something that is not of its speciatlity, Can you spot the code smell?

ANS: the initialize() function !

Why should the user_interface be involved with any other thing beside taking inputs???
WHY DOES IT HAVE TO INITIALIZE?

Abstraction principle is not followed here!
Because user_interface should be only resposible for two things:
1. taking inputs
2. passing these inputs into the 'register' logic 

-> Should'nt the initialization 'logic' be handled by the LogicClass? ---> YES 
-> if Abstraction principle was adopted/followed, you'd try to make logic itself to be the one responsible for initializing the database


"""


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



    
    
    
     
    




