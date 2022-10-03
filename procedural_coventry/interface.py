""" This is to accept user inputs from keyboard"""
from process import process_user_registration

def request_registration():
    username = input("To register, enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    process_user_registration(username, email, password)
    display("Your account has been created.")

def display(result):
    print(result)