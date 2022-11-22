

import sys
# import os
# sys.path.insert(1, os.path.join(sys.path[0], '..'))

# # import sys
# import os
# sys.path.insert(1, os.path.join(sys.path[0], '/../'))

from LogicClass import LogicClass
class UserInterface:

    def __init__(self):
        self.logicObj = LogicClass() # Composition again!! (tight coupling)
    
    def handle_register_inputs(self):
        un = input("Enter your un: ") 
        ps = input("Enter your ps: ")
        """
        [IN DEVELOPEMENT] This asserted exception equals a "flash message" on a real application
        for example: if there is an error/failure flash msg as a result from a validation check on the length of an input field 
        
        [IN TEST] it means that im "verifying" that this assertion/check is added to development code as expected  
        """
        assert len(ps) in range(4,9), "Must be between 4-8"        
        ps = int(ps)
        return un, ps



    def handle_register(self, un, ps): # Delegation/Pass-through function! (with no extra logic)
        # flag = self.logicObj.register(un, ps)
        # if flag: # LoD=Loose Coupling: accessing one dependnecy only inwards (one "dot" access opertor)
        if self.logicObj.register(un, ps): # LoD=Loose Coupling: accessing one dependnecy only inwards (one "dot" access opertor)
            return "Your account has been created", print
        return "[ERROR] An account with this name already exists.", sys.exit


    
# Driver
# UI = UserInterface()
# UI.handle_register_inputs()