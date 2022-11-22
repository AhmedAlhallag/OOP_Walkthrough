import unittest
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))



from UserInterface import UserInterface


import unittest.mock as mock


"""
============== (Unit test) UI ===================

===================================
= What are the dependencies in LogicClass?
> LogicClass (with the CRUD; read, write)

==================================
= What are we unit-testing?

=> [TODO] Can we create an object of this class ?
    Hint: Just Like the composition case in test_LogicClass.py
    
=> handle_register_inputs: 
    Test cases:
    - FrontEnd element testing: (via Terminal-based simulation to real UI in app development)
        [TODO] 1. Assert that inputs exist and were called with specific arguments (prompts), 
        Hints:
         
        => Use a mock, it does not matter what it returns, just use ".assert_called_with(<exact prompt used in implementation>)"
        => patch the input function with created mock 
        => Note: input can be found in 'builtins.input'
        
        2. Verify that Validation on password length to be between 4-8 is implemented 
        
        3. [TODO] Verify that Validate on username length is to be  implemented as follows:
            > No white spaces 
            > alphanumerical
            > a length of 4-16 chars
            > no special characters
            - You can create a separate method for validating the username input field purpose  
                
        
        
=> [TODO] handle_register (delegation)
    Test cases:
    - test the extra logic provided by the delegation function
    Hint: 
    > should we mock/decouple the .register from the within the handle_register?
    > What values should we fake return for that .register method?
"""



# test suite --> testing methods/functions for a certain unit (class)
class TestUIClass(unittest.TestCase):
    """
    [Activity] The same process to mock "Composition" based objects we used in unit testing LogicClass
    """
    @classmethod
    def setUpClass(self):
        
        # mock DataAccess
        self.mockedLogicClassObj = mock.Mock() 
        self.mockedLogicClassObj.return_value.register.side_effect = [True, False] # hard-coded test list 

        # during the execution of the constructor (while the logicClass object is being created) "replace/patch" the REAL DataAccessObject with our FAKE one
        
        with mock.patch("UserInterface.LogicClass", self.mockedLogicClassObj):
            
            # Happy path testing 
            # instantiation/object creation line
            self.UIObj = UserInterface()
            # self.logicObj.temp_users = mockedDataAccessObj.read()
            # breakpoint() # pdb -> python interactive debugger --> terminal
         
    
    def test_canCreateObject(self):
        # sad path test --> creating an object WITH arguments passed 
        with self.assertRaises(TypeError):
            UserInterface("Dummy")
            
    
    def test_UIInputFieldsExist(self):
        mockedInput = mock.Mock()
        mockedInput.input.side_effect = ["AnyValue", "123"] 
        # breakpoint()
        
         
        # with mock.patch("builtins.input", mockedInput.input) as mocked:
        #     self.UIObj.handle_register_inputs()
        #     # mocked.assert_called_with("Enter your un: ")
        #     mockedInput.input.assert_called_with("Enter your ps: ") # assert that password is actually request in the front end 
    
        # ALTER: using magic mocks 
        mockedInputFunc = mock.MagicMock( side_effect = ["AnyValue", "1223"]  )    
        with mock.patch("builtins.input", mockedInputFunc):
            self.UIObj.handle_register_inputs()
            # mocked.assert_called_with("Enter your un: ")
            mockedInputFunc.assert_called_with("Enter your ps: ") # assert that password is actually request in the front end 
            
    def test_VerifyValidationOnPasswordInputField(self):
        """
        # validation on the entered password: MUST be numbers only between 4-8
        [TODO NEXT] validation on the entered username:
            > username needs to be alphanumerical
            > a length of 4-16 chars
            > no special characters
            - You can create a separate method for validating the username input field purpose 
        """
        # valid -> 4 

        # validation on the entered password: MUST be numbers only between 4-8
        # valid
        mockedInputFunc = mock.MagicMock( side_effect = ["AnyValue", "1232"]  )    

        with mock.patch("builtins.input", mockedInputFunc):
            # Happy path: No errors
            self.UIObj.handle_register_inputs()
        
        
        mockedInputFunc = mock.MagicMock( side_effect = ["AnyValue", "1"]  )    
        # Sad Path: Expects to throw an error for this test path to succeed 
        with mock.patch("builtins.input", mockedInputFunc):
            with self.assertRaises(AssertionError):
                self.UIObj.handle_register_inputs()
            
            
    def test_VerifyValidationOnUsernameInputField(self):
        # Try this yourself!
        pass

    def test_handle_register(self):
        """
        Testing Flash messages (success/failure) 
        """
        # True 
        self.assertEqual(self.UIObj.handle_register("testUserSuccess","testPassSuccess")[0], "Your account has been created")
        # False 
        self.assertEqual(self.UIObj.handle_register("testUserFail","testPassFail")[0], "[ERROR] An account with this name already exists.")
        
# needed to be seen by the "coverage" CLI based module, to calculate percentage of test coverage
unittest.main()