from UserInterface import UserInterface

# ================== system Initialization =======================
ui = UserInterface()
ui.check_current_loggedIn()
# ================== Driver Code ==============================

def display_options():
    print("~~~~~~~ Blog App Menu ~~~~~~~")
    prompt = ""
    if not ui.check_current_loggedIn():
        menu = """Enter one of the commands in the brackets:
            
            [CA] Create Account
            [LI] Login
            
            {prompt}:> 
            """
    else:
        prompt = f"[LOGGED IN AS #{ui.get_current_loggedIn_username()}]"
        menu = f"""Enter one of the commands in the brackets:
            
            [LO] Logout
            [VB] View Blog Post
            [CP] Create A Blog Post
            
            {prompt}:> 
            """
    return menu
        
def handle_command(rep):
    rep = rep.upper()
    flash_msg=  "Unkown Command."
    if rep == "CA":
        un, ps = ui.handle_register_inputs()
        flash_msg =  ui.handle_register(un, ps)
    elif rep == "LI":
        un, ps = ui.handle_login_inputs(un, ps)
        flash_msg=  ui.handle_login(un, ps)
    elif rep == "LO":
        flash_msg = ui.logicObj.handle_logout()
    elif rep == "CP":
        flash_msg= ui.logicObj.handle_create_post()
    elif rep == "VB":
        pass
    return flash_msg

print("Welcome to the best Blog App System! \n(To exit type 'exit')\n")

rep = None

while rep != "exit":
    menu = display_options()
    rep = input(f"{menu}")
    response = handle_command(rep)
    print(response)

