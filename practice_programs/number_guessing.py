import random


def Guess_number():

    while True:
        User_num = int(input("Guess The Number btw (0-10) : "))
        random_number = random.randint(0,10)
        print("Your Number is ",User_num)
        print('Random Number is ',random_number)
        if User_num == random_number:
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-==-=-=-=-=-=--=-=-=-=-=-=-=-=-")
            print(f"!! You Guess Correct is {User_num} = {random_number}  you won!!")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-==-=-=-=-=-=--=-=-=-=-=-=-=-=-")


        elif User_num != random_number:
            print(">_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>__>_")
            print(f"!! You Guess wrong is {User_num} != {random_number} !!")
            print(">_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>__>_")


        elif (0<=User_num>=10):
            print("Please Choose number between (0-10 ) ,") 

        
        else:
            print("Invalid input... please give correct nnumber")    


p1 = Guess_number()
print(p1)