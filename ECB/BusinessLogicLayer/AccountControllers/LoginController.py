"""

Control Flow:
ECB:

Boundary -> Controller -> Entity
"""

from BusinessLogicLayer.AccountControllers.baseAccountController import baseAccountController 
class LoginController(baseAccountController): # inheritiung 

    def login(self, un, ps):
        """
        Extra return objects are needed since we have multiple "False/Error" conditions

        """
        idx, userFound = self.userExists("un",un, self.accountObj.get_users())
        if userFound:
            if self.accountObj.temp_users[idx]['ps'] == ps:
                self.accountObj.set_user(un, ps)
                return "[LOGGED_IN] You are logged in.", True 
            return "[WRONG_PASS] The password you entered is incorrect.", False         
        return "[NOT_REGISTERED] You have to register first.", False         
   
       
    def logout(self):
        self.accountObj.logout()
    
    def check_loggedin(self):
        return self.accountObj.check_loggedin()
    def get_username(self):
        return self.accountObj.username
    """
    Discussion: should we place the same def of userExist inside LoginController?
    --> common attributes/operations? put them in a super class! 
    
    """
