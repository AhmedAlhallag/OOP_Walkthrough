import unittest
from DataAccess import DataAccess
import unittest.mock as mock


"""
================================ UNIT TESTING CRUD files are useless!! ================== 


===================================
= What are we unit-testing?
------> decouple all dependnecies ! (CRUD/Database: data_resources: JSON files )

===> Create an object [DONE]
==> prepare_connection [DONE]
==> open/read
==> open/write  
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
        # D:\\2022\\OOP_Motiv\\OOP_Refactored_v1_with_tests\\fake.json
        self.assertEqual(self.dataAccObj.stored_datafile_path, self.dataAccObj.prepare_connection("fake.json"))
        # HArd coding? 
        """
        I KNOW TOO MUCH DETAIL ABOUT IMPLEMENTATION !! --> TYPES: WHITE BOX TESTING[UNIT, INTEGATION, SYSTEM] <-> BLACK BOX TESTING 
        """
        self.assertEqual("D:\\2022\\OOP_Motiv\\OOP_Refactored_v1_with_tests\\fake.json", self.dataAccObj.prepare_connection("fake.json"))
        
        
        # Happy path in REAL DB scenario 
        config = {
            "host": "localhost",
            "port": 3306,
            "dbname":"dbname",
            "user": "root"
            
        }
        # a real connection object (assertNotNone) 
        # Sad path
        config = {
            "host": "localhost",
            "port": 3307,
            "dbname":"_",
            "user": "user"
            
        }
        # make sure that there is an error being raised if the connection fails --> e.g.: false config 
        
        
    def test_read(self):
        # file processing mocks (MagicMocks) -->
        # --> mock open function --> (txt) read, write, (json) -> load, dump 

        mockedOpen = mock.MagicMock()
        
        mockedJsonLoad = mock.MagicMock( side_effect = [ [{'un': 'testUser', 'ps': 123}] ] )

        with mock.patch("builtins.open",mockedOpen):
            with mock.patch("DataAccess.json.load", mockedJsonLoad):
                data  = self.dataAccObj.read()
                # print(data)
                self.assertListEqual(data,[{'un': 'testUser', 'ps': 123}])
                
    
        
    def test_read_2(self):
        # mock anythign related to File (text, json, xml, etc..) processing: --> MagicMock -> mock_open(), mock_read, mock_write, mock_load, mock_dump 
        
        MockedOpen = mock.MagicMock() # open -->  MockedOpen
        
        MockJsonLoad = mock.MagicMock(side_effect = [ [{'un': 'testUser', 'ps': 123}]  ]  )
        
        with mock.patch("builtins.open", MockedOpen):
            with mock.patch("DataAccess.json.load", MockJsonLoad):
                data = self.dataAccObj.read()
                self.assertEqual(data,  [{'un': 'testUser', 'ps': 123}]  )
                
        