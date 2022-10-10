"""
Clean approach: Enforcing rules to abide by! + The answer: "What goes where!"

Client code Accessing the outermost module only!
and hence every other module is going one-level deep ONLY inwards 
(no pypassing is happening! horaay! we managed to build a system respspects the levels and responsibilties of every layer/module)
"""

from user_interface import handle_register, handle_register_inputs, initialize

# 1) initialize the system 

initialize()

# 2) take input
un, ps = handle_register_inputs()

# 3) perform registration

msg, do =  handle_register(un, ps)

print(msg)
do()

