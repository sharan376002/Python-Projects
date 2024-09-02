i=4
j=1
for row in range(7):
    for col in range(5):
        if(col==0 or  (col==4 and(row!=4 and row!=5 and row!=6)or (row==0 and (col>0 and col<4))) or (row==3 and (col>0 and col<4)) ):
            print("*",end=" ")
        elif(row==i and col==j):
            print("*",end=" ")
            i+=1
            j+=1
        else:
            print(end="  ")
    print()            