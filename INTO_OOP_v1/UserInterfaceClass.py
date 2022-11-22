import sys
from LogicClass import LogicClass
class UserInterface:
    """
    [Activity]: attempt to implement this class based on the procidural version
    Note: We now no longer to 'initialze' any list! we seperated that concern
    And placed it into LogicClass
    """
    def __init__(self):
        """
        [Question]: is there anything that needs to be initialzed here?
        Do we need the constructor in anything?
        
            [Bad Design]
        Solution1: We need the LogicClass to access the register method from it
        We can store a copy of the object inside the UserInterface constructor 
        
        
        Why is this bad?
        1. enforcing Composition , where it is logically not needed -> tight coupled
        2. Does 'storing' a reference of logicClass is really necessery here? 
        """

        self.logicObj = LogicClass() # Composition again!! (tight coupling)
    
    def handle_register_inputs(self):
        un = input("Enter your un: ")
        ps  = input("Enter your ps: ")
        return un, ps



    def handle_register(self, un, ps):
        if self.logicObj.register(un, ps):
            return "Your account has been created", print
        return "[ERROR] An account with this name already exists.", sys.exit


    
    
        