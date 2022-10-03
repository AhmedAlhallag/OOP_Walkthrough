""" This is to register a user and manipulate the user data """
# empty list
users = []
# empty dictionary
user_data = {}
def upload_users_list(list):
    users = list    
#to register a new user
def process_user_registration(u_name, the_email, pwd):
    user_data['username'] = u_name
    user_data['email'] = the_email
    user_data['password'] = pwd
    users.append(user_data)
def get_users():
    return users