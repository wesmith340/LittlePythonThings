# Class:      CS697 
# Assignment: CW3
# Author:     Weston Smith

import re

# Main
def Main():
    password = input("Enter a string for password: ")
    if (CheckPassword(password)):
        print("Valid password")
    else:
        print("Invalid password")

# Checks if a password is alphannumeric, has at least 2 numbers, one uppercase letter 
#   and is at least 8 characters long
def CheckPassword(password):
    if re.search("^[0-9a-zA-Z]{7}[0-9a-zA-Z]+",password) and str.islower(password) == False:
        if len(re.sub("[a-zA-Z]+","", password)) >=2:
            return True
    return False
    
Main()