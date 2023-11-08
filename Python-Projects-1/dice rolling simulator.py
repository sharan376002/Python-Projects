 # import Random
# define the function to roll the dice
# create the dictionary that will have the drawing of the dice 
# and create teh while loop the continously run

import random

def roll_dice():

    dice_drawing = {
            1: (
               ".____________.",
               "|            |",
               "|     1      |",
               "|     0      |",
               "|____________|",
            ), 
              2: (
               ".____________.",
               "|  0         |",
               "|     2      |",
               "|         0  |",
               "|____________|",
            ), 

             3: (
               ".____________.",
               "|     0      |",
               "|     0   3  |",
               "|     0      |",
               "|____________|",
            ), 

              4: (
               ".____________.",
               "|     4      |",
               "|   0  0     |",
               "|   0  0     |",
               "|____________|",
            ), 

              5: (
               ".____________.",
               "|            |",
               "|   0  5  0  |",
               "|   0  0  0  |",
               "|____________|",
            ), 

             1: (
               ".____________.",
               "|      6     |",
               "|    0 0 0   |",
               "|    0 0 0   |",
               "|____________|",
            ),                 
    }

    roll = input("Roll the Dice (Yes/No) ? :")

    while roll.lower() == "yes".lower():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        print("Dice Rolled {} and {} ".format(dice1,dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))


        roll = input("Roll again (yes/No) ? :")


roll_dice()
