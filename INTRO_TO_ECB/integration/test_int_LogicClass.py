import unittest
from LogicClass import LogicClass
from DataAccess import DataAccess
# import unittest.mock as mock # comment this! we need the real dependency to be called internally

"""
===================================
= What are we integration-testing?

--> YES, BUT: 
Yes we mock, but not the "technical" meaning of mocking 
We are mocking by using something called: "REAL TEST DATABASE" (another example of a fixture)

===================================
Edge (Test) Cases:

=> 1. Can we create an object of this class ?
-> 2. check that created objects are of correct types! 
=> 3. register: 1. register  is done successfully, 2. already registered user cannot register again
=> 4. user exists: check if a user exists or not  



"""

class TestIntegrationLogicClass(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        #Overwrite temp_users [BECAUSE OF COMPOSIITION! See how composition can still be annoying even in integration test..]
        da = DataAccess("test_user.json")
        self.logicObj = LogicClass()
        self.logicObj.data_access_obj=  da
        self.logicObj.temp_users = da.read()
    
    
    def test_checkCorrectTypes(self):
        self.assertIsInstance(self.logicObj, LogicClass)
        self.assertIsInstance(self.logicObj.data_access_obj, DataAccess)

        
    
    def test_UserExists(self): 
        self.assertTrue(self.logicObj.userExists("un", "jamal"))
        self.assertFalse(self.logicObj.userExists("un", "not in db"))

    def test_registerWhenUserAlreadyExists(self):

        self.assertFalse(self.logicObj.register("jamal",123))
        
    
    def test_registerNewUser(self):
        self.assertTrue(self.logicObj.register("NewUser",123))
        
        
        