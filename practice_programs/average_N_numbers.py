num = int(input("Enter how may number wnt average..? : "))

totalValue = 0

for i in range(num):
    numbers = float(input("Enter the number : "))
    totalValue+=numbers

average = totalValue/num

print(average)