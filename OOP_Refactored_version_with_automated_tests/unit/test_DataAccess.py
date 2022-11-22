import unittest
from DataAccess import DataAccess
import unittest.mock as mock


"""
================================ UNIT TESTING CRUD files are useless!! ================== 
[This unit tests is just for demonstration purposes]

===================================
= What are we unit-testing?
------> decouple all dependencies ! (CRUD/Database: data_resources: JSON files )

Edge (Test) Cases:
==> 1. Create an object [DONE]
==> 2. prepare_connection [DONE]
==> 3. open/read [DONE]
==> 4. open/write  [No need to be performed, you get the idea from edge case No.3]
"""


class TestDataAccessClass(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.dataAccObj = DataAccess("fake.json")
    
    def test_canCreateObject(self):
        # sad path     
        with self.assertRaises(TypeError) :
            DataAccess() 
    
    def test_prepareConnection(self):
        # D:\\2022\\OOP_Motiv\\OOP_Refactored_v1_with_tests\\fake.json # this is a bad test..
        self.assertEqual(self.dataAccObj.stored_datafile_path, self.dataAccObj.prepare_connection("fake.json"))
        # No Hard coding!
        """
        I KNOW TOO MUCH DETAIL ABOUT IMPLEMENTATION !! --> TYPES: WHITE BOX TESTING <-> BLACK BOX TESTING [UNIT, INTEGATION & SYSTEM exists for both of white and black box]
        We are supposed to be doing white box testing (we are aware of the implementation)
        BUT it should not be heavily tied to the OS like that!
        """
        self.assertEqual("D:\\2022\\OOP_Motiv\\OOP_Refactored_v1_with_tests\\fake.json", self.dataAccObj.prepare_connection("fake.json"))
        
        
        # ================= in a REAL DB scenario: =============
        # Happy path 
        # config = {
        #     "host": "localhost",
        #     "port": 3306,
        #     "dbname":"dbname",
        #     "user": "root"
            
        # }
        # # a real connection object (assertNotNone) 
        # # Sad path
        # config = {
        #     "host": "localhost",
        #     "port": 3307,
        #     "dbname":"_",
        #     "user": "user"
            
        # }
        # make sure that there is an error being raised if the connection fails --> e.g.: false config 
        # ===========================================
        
    def test_read(self):
        # file processing mocks: "MagicMocks"
        # --> mock open function --> (txt) read, write, (json) -> load, dump 

        mockedOpen = mock.MagicMock()
        
        mockedJsonLoad = mock.MagicMock( side_effect = [ [{'un': 'testUser', 'ps': 123}] ] )

        with mock.patch("builtins.open",mockedOpen):
            with mock.patch("DataAccess.json.load", mockedJsonLoad):
                data  = self.dataAccObj.read()
                self.assertListEqual(data,[{'un': 'testUser', 'ps': 123}])
                
    
        
    def test_read_2(self):
        # mock anything related to File (text, json, xml, etc..) processing: --> MagicMock -> mock_open(), mock_read, mock_write, mock_load, mock_dump 
        
        MockedOpen = mock.MagicMock() # open -->  MockedOpen
        
        MockJsonLoad = mock.MagicMock(side_effect = [ [{'un': 'testUser', 'ps': 123}]  ]  )
        
        with mock.patch("builtins.open", MockedOpen):
            with mock.patch("DataAccess.json.load", MockJsonLoad):
                data = self.dataAccObj.read()
                self.assertEqual(data,  [{'un': 'testUser', 'ps': 123}]  )
                
        