import unittest
from LogicClass import LogicClass
from DataAccess import DataAccess
# import unittest.mock as mock # comment this! we need the real depenednency to be called interanally

"""
===================================
= What are we integration-testing?

=> Can we create an object of this class ?
-> check that created objects are of correct types! 
=> register: 1. regsiter  is done successfully, 2. already registered user cannot register again
=> user exists: check if a user exists or not  

=====================================

Do we use mocking for intergations test?
--> YES AND NO 
Yes we mock, but not the "technical" meaning of mocking 
We are mocking by using something called "REAL TEST DATABASE "



"""

class TestIntegrationLogicClass(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        #Overwrite temp_users [BECAUSE OF COMPOSIITION!]
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
        # self.mockedDataAccessObj.return_value.findBy.side_effect = [0,-1] 
        self.assertTrue(self.logicObj.register("NewUser",123))
        # self.logicObj.data_access_obj.write.assert_called() # assert_called is part of the mocking object
        # self.logicObj.data_access_obj.write.assert_called_once_with(self.logicObj.temp_users)
        
        
        