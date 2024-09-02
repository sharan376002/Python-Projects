
# i = 0
#j = 4
for row in range(7):
    for col in range(5):
        if (col==0 or row ==col+2) or (col==2 and row==2) or (col==3 and row==1) or (col==4 and row==0) :
            print("*",end=" ")
        # elif(row==i and col==j)
          #  print("*",end=" ")
        #  i=i=1
        # j=j-1   
        else:
            print(end="  ")    
    print( )   