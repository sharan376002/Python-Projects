# calculate the numberbetween the twon days

from datetime import date

first_date_value = input("Enter the first date in (yy/mm/dd) : ")
first_year, first_month, first_day = map(int, first_date_value.split("/"))
first_date = date(first_year + 2000, first_month, first_day)

second_date_value = input("Enter the second date in (yy/mm/dd) : ")
second_year, second_month, second_day = map(int, second_date_value.split("/"))
second_date = date(second_year + 2000, second_month, second_day)

diff = first_date - second_date 

print(abs(diff.days), "days")