i=1
j=1
for row in range(6):
    for col in range(6):
        if((col==0 or col==5)):
            print("*",end=" ")
        elif(col==i and row==j):
            print("*",end=" ") 
            i=i+1
            j=j+1
        else:
            print(end="  ")    
    print( )        