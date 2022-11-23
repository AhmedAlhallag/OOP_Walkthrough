# from LogicClass import LogicClass
"""
# (Gateway) Boundary: Any route/input_taking/dispatch/action functions related to a certain use case 

"""
class UserInterface:

    def __init__(self, accountObj,blogObject):
        self.accountObj = accountObj
        self.blogObject= blogObject
    
    
    
    # Blog ===========================================
    def handle_create_post_inputs(self):
        title = input("Enter blog title: ") 
        body = input("Enter blog body: ")
        return title, body
    
    def handle_create_post(self):
        flash_msg = "Something went wrong..."
        if self.accountObj.check_loggedin():
            title, body = self.handle_create_post_inputs()
            self.blogObject.createBlogPost(title, body)
            flash_msg = "Blog Post Created!"
            return flash_msg
        return flash_msg
   
    def handle_display_blogs(self):
        flash_msg = "Something went wrong..."
        if self.accountObj.check_loggedin():
            blogs = self.blogObject.get_all_blogs_for_a_user()
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

        
    

    
        
    
        