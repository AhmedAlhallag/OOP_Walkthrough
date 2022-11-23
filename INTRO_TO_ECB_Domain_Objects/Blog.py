
# from DataAccess import DataAccess 

class Blog:
    def __init__(self, dataAccessObject, accountObject): 
        
        # self.data_access_obj_blog = DataAccess('blog.json')
        self.data_access_obj_blog = dataAccessObject
        self.temp_blogs = self.data_access_obj_blog.read() 
        
        # to access information from from Accont
        self.accountObject =  accountObject
        
        self.blog_title = None 
        self.blog_body = None 
        self.blog_author = None 
        
    # ================ Blog use cases ============== 
    # 1) Creating a post
    """
    # No need to check the loggedIn in the business logic, just perform the blog post creation regardless 
    # the UI will be responsible (by checking the logged in session) if a user is logged in or not first before attempting blog post creation
    """
    def createBlogPost(self, title, body):
        self.blog_title = title
        self.blog_body = body
        self.blog_author = self.accountObject.username
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
        blogs = self.data_access_obj_blog.findAll("author", self.accountObject.username, self.get_blogs())
        # if idx != -1:
        #     blog = self.get_blogs()[idx]
        #     return blog
        return blogs 
    
                
                
    def get_blogs(self): 
        return self.temp_blogs 
    
    
    
    
    