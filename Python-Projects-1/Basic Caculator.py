 # agenda
# define the function needed; add, sub , muul , div 
# print option to the user
# ask for the values 
# call the function 
# while loop to contine the function until the user finish



def add(a,b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer) + '\n')


def sub(a,b):
    answer = a - b
    print(str(a) + "+" + str(b) + "=" + str(answer) + '\n' )


def mul(a,b):
    answer = a *b
    print(str(a) + "+" + str(b) + "=" + str(answer) + '\n')

def div(a,b):
    answer = a/b 
    print(str(a) + "+ " + str(b) + "=" + str(answer) + '\n')

while True:
    

    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplacation")
    print("D. Division")
    print("E. Exit")


    choice = input("Enter the choice :")

 
    if choice == "a" or choice == "A":
        print("Addition :")
        a = int(input("Enter the value of A :"))
        b = int(input("Enter the value of B :"))
        add(a,b)


    elif choice == "b" or choice == "B":
        print("Subtraction :")
        a = int(input("Enter the Value of A :"))
        b = int(input("Enter the value of B :"))
        sub(a,b)

    elif choice == "c" or choice == "C":
        print("Multiplaction :")
        a = int(input("Enter the Value of A :"))
        b = int(input("Enter the value of B :"))
        mul(a,b)

    elif choice == "d" or choice == "D":
        print("Division : ")
        a = int(input("Enter the value of A :"))
        b = int(input("Enter the Value of B :"))
        div(a,b)

    elif choice == "e" or  choice == "E":
        print("Program Ended")
        quit()

    else:
        print("Invalid ! give a Correct choice")


 




























