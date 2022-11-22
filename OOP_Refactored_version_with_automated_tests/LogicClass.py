
from DataAccess import DataAccess # import ! == dependencies

class LogicClass:
    def __init__(self):
        """
        <mockedDataAccessObj>.<mockedRead>()
        Line 10: DataAccess Obj is a dependecy that needes to be decoupled!
        => mock/fake dataacess --> a mocked/fake .read()
        """
        self.data_access_obj = DataAccess('user.json') # Composition! (tight coupling) 
        # self.data_access_obj = data_access_obj
        self.temp_users = self.data_access_obj.read() # LoD=Loose Coupling: accessing one dependnecy only inwards (one "dot" access opertor)
        
    """
    CRUD testing(DataAccessClass): write can tested (unit+integration) there | Business Logic Testing: (optionally) write operation is "called" 
    """
    def register(self, un, ps):
        # tightly couipled dep
        if self.userExists('un', un):    
            return False
        self.temp_users.append({'un':un, "ps": ps})
        self.data_access_obj.write(self.get_users()) # LoD=Loose Coupling: accessing one dependnecy only inwards (one "dot" access opertor)
        return True
    
    """
    Notice that the dataacess object that the userexists is going to use here is the SAME mockedd object from before!
    find by is not going to be having defintiion!
    """
    def userExists(self, key, value): # Delegation/Pass-through function (with extra logic)
       
        idx = self.data_access_obj.findBy(key, value, self.temp_users)
        # print(idx)
        if idx != -1:
            return True
        return False

    """
    getters/setters --> they dont procide any additional logic --> can be skipped for unit/integration tests
    """
    def get_users(self): # getter--> Scaffolding code 
        return self.temp_users 
    
    
    
    
# Driver code 
# logicObj = LogicClass()
# print(logicObj.userExists("un", "testUsdfsfser"))
# print(logicObj)
# print(logicObj.__dict__)
# logicObj = LogicClass("Dummy") # error 


