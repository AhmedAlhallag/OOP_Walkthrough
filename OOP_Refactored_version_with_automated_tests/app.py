from UserInterface import UserInterface

ui = UserInterface()


# 2) take input
un, ps = ui.handle_register_inputs()

# 3) perform registration

msg, do =  ui.handle_register(un, ps)

print(msg)
do()

