i=0
j=0
for row in range(5):
    for col in range(5):
        if(row==i and col==j):
            print("*",end=" ")
            i+=1
            j+=1
        elif((col==4 and row==0) or (col==3 and row==1) or  (col==2 and row==2)or (col==1 and row==3)or (col==0 and row==4)):
            print("*",end=" ")

        else:
            print(end="  ")
    print()            
