from logic import register

def handle_inputs():
    un = input("Enter Un: ")
    ps = input("Enter Ps: ")
    return un, ps 

def handle_register(un,ps):
    register(un, ps)
    return "Account has been created."



