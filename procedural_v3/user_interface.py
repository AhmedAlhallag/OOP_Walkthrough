# take inputs from the end user/ client 
from logic import register
import sys
# name this file as handler.py 

def handle_register_inputs():
    un = input("Enter your un: ")
    ps  = input("Enter your ps: ")
    return un, ps

"""
logic.3.2.2) haneling the thrown error message/excpetion of the conditional in the user_interface (acting as the controller controller)
"""

"""
logic 3.2.3) perform monkey patching to garantuee that:
1. the returned message will be printed first in app.py
2. the relevant patched function will execute later on without disrupting the flow of the system (app.py)
; this way we would not need to perform an out-of-no-where if statement in the app.py! 
+ we normalized the return pattern of our function in case of: 1. success and 2. failure!

"""

def handle_register(un, ps):
    if register(un, ps):
        return "Your account has been created", print
    return "[ERROR] An account with this name already exists.", sys.exit



    
    
    
     
    




