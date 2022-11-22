# from user_interface import handle_register, handle_register_inputs, initialize
"""
See how now we will be replacing his very long pooring impoert witrh a single import of the userinterface class

+ See How we applied Asbtraction and information hiding in our client code?

+ I don't to expose the "initialize" function to the client anymore! (done in LogicClass object)

+ We don't to import ton of function!! only one class from the subseqeunt inner layer/module is enough!

"""


from UserInterfaceClass import UserInterface

ui = UserInterface()



# 1) initialize the system 

# initialize()
"""
No need to initialize anything, taken care of by the object's constructor method.
"""

# 2) take input
un, ps = ui.handle_register_inputs()

# 3) perform registration

msg, do =  ui.handle_register(un, ps)

print(msg)
do()

