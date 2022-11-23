from UserInterface import UserInterface
from Account import Account
from Blog import Blog
from DataAccess import DataAccess

# ================== system Initialization =======================
dataAccessObjectUser = DataAccess("user.json")
dataAccessObjectBlog = DataAccess("blog.json")

accountObject = Account(dataAccessObjectUser)

blogObject = Blog(dataAccessObjectBlog, accountObject)

ui = UserInterface(accountObject, blogObject)
# ================== Driver Code ==============================

def display_options():
    print("~~~~~~~ Blog App Menu ~~~~~~~")
    prompt = ""
    if not ui.check_current_loggedIn():
        menu = f"""Enter one of the commands in the brackets:
            
            [CA] Create Account
            [LI] Login
            
            """
    else:
        prompt = f"[LOGGED IN AS #{ui.get_current_loggedIn_username()}]"
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
        un, ps = ui.handle_register_inputs()
        flash_msg =  ui.handle_register(un, ps)
    elif rep == "LI":
        un, ps = ui.handle_login_inputs()
        flash_msg=  ui.handle_login(un, ps)
    elif rep == "LO":
        flash_msg = ui.handle_logout()
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

