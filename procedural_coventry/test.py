""" This is to run the program """
from interface import request_registration
from process import get_users, upload_users_list
from data import read_users, write_users
#to run the program
if __name__ == '__main__':
    # retrieve a list of users (data module)
    list = read_users()
    # upload a list of users to be processed (process module)
    upload_users_list(list)
    # request for a registration with a new users' details (interface module)
    # register the user (process module)
    request_registration()
    
    print("Before  commiting into database...")
    print("Current user base in the logic layer:" ,get_users(), sep="\n")
    print("Current user base in the data layer:" ,read_users(), sep="\n")
    print("\n")
    
    # update the users list (data module)
    write_users(get_users())
    
    print("After  commiting into database...")
    print("Current user base in the logic layer:" ,get_users(), sep="\n")
    print("Current user base in the data layer:" ,read_users(), sep="\n")
    print("\n")
    
    
    # print(users)