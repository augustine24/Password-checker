import re
Password = input("Please enter your password: ") 
if len(Password) < 4 or len(Password)> 20:
    print("Your password must have 4 - 20 characters. Please try again.")
#The above line is a conditional that determines the appropriate length of the password.
if not re.search("[A-Z]", Password):
    print("Your password must include uppercase letters.")
#The above line is a conditional that forces the user to use uppercase letters.
if not re.search("[0-9]", Password):
    print("Your password must include numbers.")
#The above line is a conditional that forces the user to use numbers in their password.
if not re.search("[!@#$%^&*]", Password):
    print("Your password must include special characters.")
#The above line is a conditional that forces the user to use special characters in their password.
if re.search("[ ]", Password):
    print("Your password cannot have spaces.")
#This conditional bans spaces from being used in the password.
if re.search ("[A-Z]", Password) and re.search("[0-9]", Password) and re.search("[!@#$%^&*]", Password) and not re.search("[ ]", Password):
    print("Password succesfully created.")
#This conditional allows the password to be succesfully created once all conditions are met. This entire code is message based, so there is more to a password
#creating mechanism than this.
#Enter your password until it's valid. Enjoy!
