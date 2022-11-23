# from LogicClass import LogicClass
class UserInterface:

    def __init__(self, logicObj):
        self.logicObj = logicObj
        # self.logicObj = LogicClass() 
    
    # Register ==================================================================
    def handle_register_inputs(self):
        un = input("Enter your un: ") 
        ps = input("Enter your ps: ")
        assert len(ps) in range(4,9), "Must be between 4-8"        
        ps = int(ps)
        return un, ps
    

    def handle_register(self, un, ps): 
        if self.logicObj.register(un, ps): 
            return "Your account has been created"
        return "[ERROR] An account with this name already exists."

    # Login ==========================================================    
    def handle_login_inputs(self):
        un = input("Enter your un: ") 
        ps = int(input("Enter your ps: "))
        return un, ps

    def handle_login(self, un, ps): 
        flash_msg, status = self.logicObj.login(un, ps)
        return flash_msg

    def handle_logout(self):
        self.logicObj.logout()
        return "Logging Out..."
    
    def check_current_loggedIn(self):
            # Delegation
        return self.logicObj.check_loggedin()
    
    def get_current_loggedIn_username(self):
        return self.logicObj.username
        
    
    # Blog ===========================================
    def handle_create_post_inputs(self):
        title = input("Enter blog title: ") 
        body = input("Enter blog body: ")
        return title, body
    
    def handle_create_post(self):
        flash_msg = "Something went wrong..."
        if self.logicObj.check_loggedin():
            title, body = self.handle_create_post_inputs()
            self.logicObj.createBlogPost(title, body)
            flash_msg = "Blog Post Created!"
            return flash_msg
        return flash_msg
   
    def handle_display_blogs(self):
        flash_msg = "Something went wrong..."
        if self.logicObj.check_loggedin():
            blogs = self.logicObj.get_all_blogs_for_a_user()
            flash_msg = ""
            print(blogs)
            for blog in blogs:
                flash_msg += f""" 
                ===================================
                Blog title: {blog['title']},
                Blog body: {blog['body']}
                ===================================
                \n
                """
        return flash_msg

        
    

    
        
    
        