from PresentationLayer.AccountBoundary.LoginUI import LoginUI
from PresentationLayer.AccountBoundary.RegisterUI import RegisterUI
from BusinessLogicLayer.AccountControllers.LoginController import LoginController
from BusinessLogicLayer.AccountControllers.RegisterController import RegisterController
from DataAccessLayer.Entities.Account import Account
from DataAccessLayer.Entities.Blog import Blog
from DataAccessLayer.DataAccess import DataAccess

# ================== system Initialization =======================
# DataAccess 
dataAccessObjectUser = DataAccess("user.json")
dataAccessObjectBlog = DataAccess("blog.json")

# Entity 
accountObject = Account(dataAccessObjectUser)

# controller 
loginControllerObj = LoginController(accountObject)
registerControllerObj = RegisterController(accountObject)


# Boundary 
loginUi = LoginUI(loginControllerObj)
regUi = RegisterUI(registerControllerObj)


blogObject = Blog(dataAccessObjectBlog, accountObject)

# ================== Driver Code ==============================

def display_options():
    print("~~~~~~~ Blog App Menu ~~~~~~~")
    prompt = ""
    if not loginUi.check_current_loggedIn():
        menu = f"""Enter one of the commands in the brackets:
            
            [CA] Create Account
            [LI] Login
            
            """
    else:
        prompt = f"[LOGGED IN AS #{loginUi.get_current_loggedIn_username()}]"
        menu = f"""Enter one of the commands in the brackets:
            
            [LO] Logout
            [VB] View Blog Post
            [CP] Create A Blog Post
            
            """
    return menu, prompt
        
def handle_command(rep):
    rep = rep.upper()
    flash_msg=  "Unkown Command."
    if rep == "CA":
        un, ps = regUi.handle_register_inputs()
        flash_msg =  regUi.handle_register(un, ps)
    elif rep == "LI":
        un, ps = loginUi.handle_login_inputs()
        flash_msg=  loginUi.handle_login(un, ps)
    elif rep == "LO":
        flash_msg = loginUi.handle_logout()
    elif rep == "CP":
        flash_msg= ui.handle_create_post()
    elif rep == "VB":
        flash_msg = ui.handle_display_blogs()
    return flash_msg

print("Welcome to the best Blog App System! \n(To exit type 'exit')\n")

rep = None

while rep != "exit":
    menu, prompt = display_options()
    rep = input(f"{menu}\n{prompt}:> ")
    response = handle_command(rep)
    print(response)

