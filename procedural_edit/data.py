

users_in_database = [{'un':'haidy',"ps":123}]

def read():
    return users_in_database

def write(alist):
    global users_in_database
    users_in_database = alist