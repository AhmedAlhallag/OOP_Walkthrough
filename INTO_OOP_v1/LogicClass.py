
from DataAccess import DataAccess
class LogicClass:
    
    def __init__(self):
        """
        [Activity]: the same way you used instance variables to elimnate the global stored_file_path   
        do the same thing for temp_users
        
        [Eliminate Gobals using instance variables AGAIN] initializer can be used to read the list of users 
        """
        # TODO
        """
        
        # where does the value of self.temp)user come from?
        Should we consider having it to be initialzied by the user_interface? 
        (Check why this was bad design in procuidral versioon)
        or better have it initialized within the logic class
        """
        
        """
        Solution: we only need the "read()" from DataAcces, but now its a method and the only possible way to
        access this method is via using a DataAccess Object
        
            [BAD DESIGN]
            Using composition --> Tight Coupling 
        """
        # initialization: done automatically once an object of LogicClass is created
        self.data_access_obj = DataAccess('user.json') # composition !! (not always is bad , but in this case it is)
        self.temp_users = self.data_access_obj.read()
        
    
    # no need for this anymore
    # def update_current_users_from_database(self):
    #     self.temp_users  = read("user.json")
    """
    [Activity] TODO: Convert the rest of the functions from logic.py into OOP based method inside the LogicClass
    """
 

"""
Driver/Testing/Client Code
"""
        
# logicObj = LogicClass()

# print(logicObj.temp_users)

        
        
    