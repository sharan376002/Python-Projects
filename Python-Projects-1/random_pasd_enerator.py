import random
import string
while True:
    
    lenth = int(input('Enter the length of the password: '))
    
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    number = string.digits
    symbols = string.punctuation

    all = upper + lower+ number+ symbols

    password = "".join(random.sample(all,lenth))

    print(password)