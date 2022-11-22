import unittest
from LogicClass import LogicClass
import unittest.mock as mock


"""
(Unit test): having NO external dependencies involved!

- What are types of dependencies?

=> T1: injected dependencies [DI-Association] ==> easiest to decouple
=> T2: internal (function/method call - an object creation[composition]) => hardest to decouple 

================================== 

- How to mock dependencies:
T1[EASY]: 1. mock objects: +behaviour, +operations ON THE FLY!
T2[HARD]: 1. mock objects + 2. patching(replacing a certain function in run time ) context [context:during the execturiotn of a functio]



= What are the dependencies in LogicClass?
> DataAccess (with the CRUD; read, write)

===================================
= What are we unit-testing?

=> Can we create an object of this class ?
=> register: 1. regsiter  is done successfully, 2. already registered user cannot register again
=> user exists: check if a user exists or not  
=> Contained list is not empty + contained List is an iterable (fetched/read)


=> [added feature] login => 1. login is done successfuly, 2. user should be regsitered before logging in, 
3. if a user is logged in, he cannot log in again at the same time/session (unless he logs out)
4. if a user is logged in, no OTHER user can login at the same time/session




====================================
General Note on Unit vs Integration
unit testing <=> integration testing (unit testing + having actual dependencies) 

"""


# test suite --> testing methods/functions for a certain unit (class)
class TestLogicClass(unittest.TestCase):
    
    # setup: happens before the run of every test method 
    # setupclass: happens only once before the execution of all test methods
    @classmethod
    def setUpClass(self):
        """
        To understand line 60: Take a look at the implementtaion of the LogicClass Constructor
        > first it calls the DataAccess Class --> Mock object is called => self.mockedDataAccessObj.return_value
        > second it calls read from the data_access_obj --> mocked read is called from Mock object => self.mockedDataAccessObj.return_value.read.return_value
        """        
        # mock DataAccess
        self.mockedDataAccessObj = mock.Mock() 
        self.mockedDataAccessObj.return_value.read.return_value = [{'un': 'testUser', 'ps': 123}] # hard-coded test list 
        
        # during the execution of the constructor (while the logicClass object is being created) "replace/patch" the REAL DataAccessObject with our FAKE one
        
        with mock.patch("LogicClass.DataAccess", self.mockedDataAccessObj):
            
            # Happy path testing 
            # instantiation/object creation line
            self.logicObj = LogicClass()
            # self.logicObj.temp_users = mockedDataAccessObj.read()
            # breakpoint() # pdb -> pytgon interactive debugger --> terminal
         
    
    def test_canCreateObject(self):
        # sad path test --> creating an object WITH arguments passed 
        with self.assertRaises(TypeError):
            LogicClass("Dummy")
            
    def test_TempUsersListNotEmptyAndIterable(self):
        # happy path testing
        self.assertIsNotNone(iter(self.logicObj.temp_users))
        
    def test_UserExists(self): 
        self.mockedDataAccessObj.return_value.findBy.side_effect = [0,-1]
        self.assertTrue(self.logicObj.userExists("un", "testUser"))
        self.assertFalse(self.logicObj.userExists("un", "not in db"))

    def test_registerWhenUserAlreadyExists(self):
        # self.mockedDataAccessObj.return_value.findBy.side_effect = [0,-1] 
        self.mockedDataAccessObj.return_value.findBy.side_effect = [0] 
        self.assertFalse(self.logicObj.register("testUser",123))
        
    
    def test_registerNewUser(self):
            # self.mockedDataAccessObj.return_value.findBy.side_effect = [0,-1] 
        self.mockedDataAccessObj.return_value.findBy.side_effect = [-1] 
        self.assertTrue(self.logicObj.register("NewUser",123))
        self.logicObj.data_access_obj.write.assert_called()
        self.logicObj.data_access_obj.write.assert_called_once_with(self.logicObj.temp_users)
        
        
        
        
        
    


    
    

        
    
        
            
            
            

        
        
        