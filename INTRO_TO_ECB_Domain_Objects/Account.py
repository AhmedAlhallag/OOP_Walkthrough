class Account:
    def __init__(self, dataAccessObject): 
      
        # self.data_access_obj_user = DataAccess('user.json') 
        self.data_access_obj_user = dataAccessObject
        self.temp_users = self.data_access_obj_user.read() 
       
        # attributes for user
        self.username = None 
        self.password = None 
        self.loggedIn = False
    
    def register(self, un, ps):
        idx, userFound = self.userExists('un', un, self.get_users())
        if userFound:     
            return False
        self.temp_users.append({'un':un, "ps": ps})
        self.data_access_obj_user.write(self.get_users()) 
        return True
    
    def userExists(self, key, value, alist):
        idx = self.data_access_obj_user.findBy(key, value, alist)
        if idx != -1:
            return idx, True
        return idx, False

    def get_users(self): 
        return self.temp_users 

    def login(self, un, ps):
        """
        Extra return objects are needed since we have multiple "False/Error" conditions

        """
        idx, userFound = self.userExists("un",un, self.get_users())
        if userFound:
            if self.temp_users[idx]['ps'] == ps:
                self.set_user(un, ps)
                return "[LOGGED_IN] You are logged in.", True 
            return "[WRONG_PASS] The password you entered is incorrect.", False         
        return "[NOT_REGISTERED] You have to register first.", False         

    def set_user(self, un, ps):
        self.username = un 
        self.password = ps 
        self.loggedIn = True
    
    def logout(self):
        self.username = None
        self.password = None
        self.loggedIn = False
    
    def check_loggedin(self):
        return self.loggedIn

    