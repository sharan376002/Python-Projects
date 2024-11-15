def compound_interst(principal,rate,time,compounded_per_year):
   
   rate = rate/100

   amount = principal * (1 + rate / compounded_per_year) ** (compounded_per_year * time)
   compound_interest = amount - principal
   return round(compound_interest, 2), round(amount, 2)





print("To find the compound interst calculator")

principal = float(input("Enter the initail amount"))
rate = float(input("Enter the annual rate in(%)"))
time = float(input("number of years (T)"))
compounded_per_year = int(input("Enter the number of times interest is compounded per year:"))


interest, total_amount = compound_interst(principal, rate, time, compounded_per_year)

print(f"Compound Interest: ${interest}")
print(f"Total Amount: ${total_amount}")