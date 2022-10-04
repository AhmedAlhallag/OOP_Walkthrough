# take inputs from the end user/ client 
from logic import register


def handle_register_inputs():
    un = input("Enter your un: ")
    ps  = input("Enter your ps: ")
    return un, ps


def handle_register(un, ps):
    register(un, ps)
    return "Your account has been created"



    
    
    
     
    




