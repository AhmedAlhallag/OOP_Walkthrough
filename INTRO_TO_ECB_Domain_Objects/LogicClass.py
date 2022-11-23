
# from DataAccess import DataAccess 

class LogicClass:
    def __init__(self, dataAccessObject): 
        """
        PROBLEM!
        Cannot refactor to association via this version!!! --> it is a must to eithe:
        1. create two objects of Logic Class one takes an dataaccessObject of user.json, and the other
        takes  dataaccessObject of blog.json,
        2. send a list (or a dict) of  dataaccessObjects and label it as of [0] -> DAOUser and [1] --> DAOBlog; NOT READABLE!
        3.Best solution -> refactor to ECB and use DAO pattern
        """
        
        # Reading all users into a temp_users list 
        self.data_access_obj_user = DataAccess('user.json') 
        self.temp_users = self.data_access_obj_user.read() 
        # Reading all blogs into a temp_blogs list
        
        self.data_access_obj_blog = DataAccess('blog.json')
        self.temp_blogs = self.data_access_obj_blog.read() 
        
        # attributes for user
        self.username = None 
        self.password = None 
        self.loggedIn = False
        
        self.blog_title = None 
        self.blog_body = None 
        self.blog_author = None 
        
    def register(self, un, ps):
        idx, userFound = self.userExists('un', un, self.get_users())
        if userFound:     
            return False
        self.temp_users.append({'un':un, "ps": ps})
        self.data_access_obj_user.write(self.get_users()) 
        return True
    
    def userExists(self, key, value, alist):
        idx = self.data_access_obj_user.findBy(key, value, alist)
        if idx != -1:
            return idx, True
        return idx, False

    def get_users(self): 
        return self.temp_users 

    def login(self, un, ps):
        """
        Extra return objects are needed since we have multiple "False/Error" conditions

        """
        idx, userFound = self.userExists("un",un, self.get_users())
        if userFound:
            if self.temp_users[idx]['ps'] == ps:
                self.set_user(un, ps)
                return "[LOGGED_IN] You are logged in.", True 
            return "[WRONG_PASS] The password you entered is incorrect.", False         
        return "[NOT_REGISTERED] You have to register first.", False         

    def set_user(self, un, ps):
        self.username = un 
        self.password = ps 
        self.loggedIn = True
    
    def logout(self):
        self.username = None
        self.password = None
        self.loggedIn = False
    
    def check_loggedin(self):
        return self.loggedIn

    
    # ================ Blog use cases ============== 
    # 1) Creating a post
    """
    # No need to check the loggedIn in the business logic, just perform the blog post creation regardless 
    # the UI will be responsible (by checking the logged in session) if a user is logged in or not first before attempting blog post creation
    """
    def createBlogPost(self, title, body):
        self.blog_title = title
        self.blog_body = body
        self.blog_author = self.username
        self.temp_blogs.append({'title':self.blog_title , "body": self.blog_body, "author": self.blog_author})
        self.data_access_obj_blog.write(self.get_blogs()) 
        return True 

    # 2) Display Blogs 
    def get_all_blogs_for_a_user(self):
        """
        PROBLEM: we need ALL blogs of a user (not one)
        [Design Discussion]:
        - every domain object's will have variants of search functions, so is it worth it to put all of these different search 
        functions in one DataAccess ? ANS: No ((check comment in DATA_ACCESS))
        """
        blogs = self.data_access_obj_blog.findAll("author", self.username, self.get_blogs())
        # if idx != -1:
        #     blog = self.get_blogs()[idx]
        #     return blog
        return blogs 
    
                
                
    def get_blogs(self): 
        return self.temp_blogs 
    
    
    
    
    