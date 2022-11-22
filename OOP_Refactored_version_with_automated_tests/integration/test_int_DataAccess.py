import unittest
from DataAccess import DataAccess
# import unittest.mock as mock


"""
Integration test CRUD files


===================================
= What are we integration-testing?

> Do we mock in CRUD intergationn testing???

--> YES, BUT: 
Yes we mock, but not the "technical" meaning of mocking 
We are mocking by using something called: "REAL TEST DATABASE" (another example of a fixture)

===================================

Edge (Test) Cases:
==> 1. Check correct types of all coupled dependencies are created [DONE]
==> 2. prepare_connection [DONE]
==> 3. open/read: 1. file is valid. 2. reading returned expected data (types, columns, values...)[DONE]
==> 4. open/write  [No need to be performed, you get the idea from edge case No.3]

"""


class TestIntegrationDataAccessClass(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        """
        REAL "TEST" DATABASE
        """
        self.dataAccObj = DataAccess("test_user.json")
    
    def test_prepareConnection(self):
        self.assertEqual(self.dataAccObj.stored_datafile_path, self.dataAccObj.prepare_connection("test_user.json"))
        
        
            
    def test_check_correct_type(self):
        self.assertIsInstance(self.dataAccObj, DataAccess)
        
    def test_readFileIsValid(self):
        # Happy path 
        da = DataAccess("test_user.json")
        da.read()
        # Sad path 
        with self.assertRaises(FileNotFoundError):
            da = DataAccess("fake.json")
            da.read()
            
    
        
    def test_checkReadData(self):
        data = self.dataAccObj.read()
        self.assertIn("un",data[0].keys())
        self.assertIn("ps",data[0].keys())
                
    
        
        
   
            
            
        