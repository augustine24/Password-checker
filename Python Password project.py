import re
Password = input("Please enter your password: ") 
if len(Password) < 4 or len(Password)> 20:
    print("Your password must have 4 - 20 characters. Please try again.")
if not re.search("[A-Z]", Password):
    print("Your password must include uppercase letters.")
if not re.search("[0-9]", Password):
    print("Your password must include numbers.")
if not re.search("[!@#$%^&*]", Password):
    print("Your password must include special characters.")
if re.search("[ ]", Password):
    print("Your password cannot have spaces.")
if re.search ("[A-Z]", Password) and re.search("[0-9]", Password) and re.search("[!@#$%^&*]", Password) and not re.search("[ ]", Password):
    print("Password succesfully created.")
#Enter your password until it's valid. Enjoy!
