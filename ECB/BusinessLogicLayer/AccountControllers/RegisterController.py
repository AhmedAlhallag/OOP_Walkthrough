"""

Control Flow:
ECB:

Boundary -> Controller -> Entity

"""

from BusinessLogicLayer.AccountControllers.baseAccountController import baseAccountController
class RegisterController(baseAccountController):
    
    def register(self, un, ps):
        idx, userFound = self.userExists('un', un, self.accountObj.get_users())
        if userFound:     
            return False
        self.accountObj.temp_users.append({'un':un, "ps": ps})
        # self.accountObj.data_access_obj_user.write(self.get_users())  
        self.accountObj.access_write(self.accountObj.get_users())  
        return True
        
