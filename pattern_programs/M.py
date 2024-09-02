i=1
j=5
for row in range(7):
    for col in range(7):                                          # here we can solve this problen this way too lopp is more efficient
        if(col==0 or col==6) or (row==col and (col>0 and col<3)): #or (col==5 and row==1) or (col==4 and row==2)or(col==3 and row==3):
            print("*",end=" ")
        elif(row==i and col==j):
            if j==2 and i==4 :
                break
            else:

                print("*",end=" ")
                i +=1
                j-=1
                

        else:
            print(end="  ")    
    print( )        