




for i in range(1,7):
    print("*"*i)

print("--------------------------------------------------------------")


  





#num = int(input("Enter the input :"))
for i in range(1,7):
    for j in range(1, i+1):
        print("*",end=" ")
    print( )    

print("----------------------------------------------------")

#num = int(input("Enter the input :"))
for i in range(1,8,2):
    for j in range(1, i+1):
        print("*",end=" ")
    print( )    

print("----------------------------------------------------")

for i in range(0, 7):
    for j in range(0,7-i-1):
        print(end=" ")
    for j in range(0, i+1):
        print("*",end=" ")   
    print()     