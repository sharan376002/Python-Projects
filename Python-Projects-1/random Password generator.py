# ask the user if they want to generate the password
# if yes ask for password length
# generate the password 
# print passwword 
# if the initial process is no, exit the program  

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()?|" )


def generate_password():
    password_length = int(input("How long the password you want "))

    random.shuffle(characters)

    password =[]

    for x in  range(password_length):
        password.append(random.choice(characters))
    
    random.shuffle(password)

    password="".join(password)

    print(password)



option = input("Do yiou wnat to generate the password (yes/no) ?  :")

if option == "YES".lower():
    generate_password()

elif option == "no".lower():    
    print("Ok")
    quit()

else:
    print("Invalid Input ")
    quit()
        

