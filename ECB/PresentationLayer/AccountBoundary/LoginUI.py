

"""

ECB:
Boundary -> Control 
Control -> Entity
Boundary -/-> Entity
"""

class LoginUI():
    def __init__(self, loginControllerObj):
        self.loginControllerObj = loginControllerObj

    # Login ==========================================================    
    def handle_login_inputs(self):
        un = input("Enter your un: ") 
        ps = int(input("Enter your ps: "))
        return un, ps

    def handle_login(self, un, ps): 
        flash_msg, status = self.loginControllerObj.login(un, ps)
        return flash_msg

    def handle_logout(self):
        self.loginControllerObj.logout()
        return "Logging Out..."
    
    def check_current_loggedIn(self):
            # Delegation
        return self.loginControllerObj.check_loggedin()
    
    def get_current_loggedIn_username(self):
        return self.loginControllerObj.get_username()
        