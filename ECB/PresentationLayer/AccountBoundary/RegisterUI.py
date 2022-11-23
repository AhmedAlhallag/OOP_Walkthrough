

"""

ECB:
Boundary -> Control 
Boundary -/-> Entity
"""

class RegisterUI():
    def __init__(self, registerControllerObj):
        self.registerControllerObj = registerControllerObj
# Register ==================================================================
    def handle_register_inputs(self):
        un = input("Enter your un: ") 
        ps = input("Enter your ps: ")
        assert len(ps) in range(4,9), "Must be between 4-8"        
        ps = int(ps)
        return un, ps
    

    def handle_register(self, un, ps): 
        if self.registerControllerObj.register(un, ps): 
            return "Your account has been created"
        return "[ERROR] An account with this name already exists."
