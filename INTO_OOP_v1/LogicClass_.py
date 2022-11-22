
from DataAccess import DataAccess
class LogicClass:
    
    def __init__(self):
        self.data_access_obj = DataAccess('user.json') #
        self.temp_users = self.data_access_obj.read()
        
    
    def register(self, un, ps):
      
        if self.userExists('un', un):    
            return False
        self.temp_users.append({'un':un, "ps": ps})
        self.data_access_obj.write(self.get_users())
        return True
    

    # def userExists(key, value, alist): # old signature
    def userExists(self, key, value):
       
        idx = self.data_access_obj.findBy(key, value, self.temp_users)
        if idx != -1:
            return True
        return False


    def get_users(self):
        return self.temp_users 
    

