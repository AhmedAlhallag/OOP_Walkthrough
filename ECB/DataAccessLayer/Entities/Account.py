"""
"Entities":
-> The closest thing to persistance (storage)
-> Sometimes refred to as models 
-> 1-to-1 Maps to a table structure 
-> Plain Objects: attributes and getters/setters
    
# Design Issue:
We should omit the dataaccess object from here!
"Plain Object" AKA "Entities  should NOT contain anything other than attributes and getters/setters  


=================
Where does the REAL "business" use cases go? --> INTO "Controllers"
- LoginController.py
- RegisterController.py
"""
class Account:
    def __init__(self, dataAccessObject): 
      
        # self.data_access_obj_user = DataAccess('user.json') 
        self.data_access_obj_user = dataAccessObject
        self.temp_users = self.data_access_obj_user.read() 
       
        # attributes for user
        self.username = None 
        self.password = None 
        self.loggedIn = False
        
    def get_users(self): 
        return self.temp_users 
    
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
    
    def access_write(self, alist):
         self.data_access_obj_user.write(alist)
         
    def access_findBy(self, key, value, alist):
        return self.data_access_obj_user.findBy(key, value, alist)
        

