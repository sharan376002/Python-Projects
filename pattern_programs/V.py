i=0
j=0
p=6
q=0
for row in range(7):
    for col in range(7):
        if(row==i and col==j):
            if(row==4 and col==4):
                break;
            else:
                print("*",end=" ")
                i+=1
                j+=1
        elif(col==p and row==q):
            print("*",end=" ")
            p-=1
            q+=1

        else:
            print(end="  ")
    print()            
