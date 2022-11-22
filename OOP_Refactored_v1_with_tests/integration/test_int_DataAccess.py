import unittest
from DataAccess import DataAccess
# import unittest.mock as mock


"""
Integration test CRUD files -->  REAL "TEST" DATABASE


===================================
= What are we integration-testing?

> Do we mock in CRUD intergationn testing???

--> YES AND NO 
Yes we mock, but not the "technical" meaning of mocking 
We are mocking by using something called "REAL TEST DATABASE "

==> check types are correct
===> preprare_connection
==> open/read: 1. file is valid. 2. reading returns expected data (types, columns, values...)
==> open/write  
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
        # print(data)
        # self.assertListEqual()
        self.assertIn("un",data[0].keys())
        self.assertIn("ps",data[0].keys())
                
    
        
        
   
            
            
        