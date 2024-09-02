

for row in range(7):
    for col in range(7):
       
        if (row == 0 or row == 7-2) and (col > 0 and col < 7-1) or \
           (col == 0 or col == 7-1) and (row > 0 and row < 7-2) or \
           (row == 7-3 and col == 7-3) or \
           (row == 7-1 and col == 7-2):
            print("*", end="")
        else:
            print(" ", end="")
    print()
