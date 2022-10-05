# take inputs from the end user/ client 
from logic import register

# name this file as handler.py 

def handle_register_inputs():
    un = input("Enter your un: ")
    ps  = input("Enter your ps: ")
    return un, ps

"""
logic.3.2) haneling the thrown error message/excpetion of the conditional in the user_interface (acting as the controller controller)
"""

def handle_register(un, ps):
    register(un, ps)
    return "Your account has been created"



    
    
    
     
    




