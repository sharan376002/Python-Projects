


# Loop to print the pattern
for row in range(7):
    for col in range(7):
        # Print the border of the P pattern
        if col == 0 or (row == 0 or row == 7//2) and col < 7-1 or (col == 7-1 and row < 7//2 and row != 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()









      #  if  (col==0 or (col==4 and (row==1 or row==2 ))) or ((row==0 or row==3) and (col>0 and col<4)):or (() and(row==1 and row==2 ))
    