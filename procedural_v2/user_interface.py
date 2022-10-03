# take inputs from the end user/ client 
from logic import register


def handle_register_inputs():
    un = input("Enter your un: ")
    ps  = input("Enter your ps: ")
    return un, ps


def handle_register():
    register(*handle_register_inputs())
    return "Your account has been created"



    
    
    
     
    




