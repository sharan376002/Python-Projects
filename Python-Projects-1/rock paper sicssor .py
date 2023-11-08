import random 

exit = False
user_points = 0
computer_points = 0


while exit == False:
    option = ["rock", "paper", "sicssors"]
    user_input =  input("Chose rock , paper , sicssor & Exit :")
    computer_input = random.choice(option)



    if user_input == "exit":
        print("game Ended")
        print("you won a total Score of "+ str(user_points)+"and the computer total score is "+ str(computer_points))
        exit = True 


    if  user_input == "rock":
        if computer_input == "rock":
            print("Your input is Rock")
            print("computer input is rock")
            print("It is a Tie ")
        
        elif computer_input == "paper":
            print("Your input is rock")
            print("Computer input is paper")
            print("Computer Win's")
            computer_points+= 1

        elif computer_input == "sicssor":
            print("Your input is rock ")
            print("Computer input is sicssor ")
            print("You Win's") 
            user_points += 1

    if user_input == "paper":
        if computer_input == "rock":
            print("your input is paper")
            print("computer input is rock ")
            print("You Wins")
            user_points += 1 

        elif computer_input == "paper":
            print("your input is paper")
            print("computer input is paper")
            print("It is Tie ")

        elif computer_input == "sicssor":
            print("your input is paper")
            print("computer input is sicssor ")
            print("you wins")
            computer_points += 1
       
    if user_input == "sicssor":
        if computer_input == "rock":
            print("your input is sicssor")
            print("computer input is rock")
            print("computer wins")
            computer_points +=1 

        elif computer_input == "paper":
            print("Your input is sicssor")
            print("computer input is paper ")
            print("you wins")
            user_points += 1 

        elif computer_input == "sissor":
            print("your input is sicssor")
            print("computer input is sicssor")
            print("It is tie")
