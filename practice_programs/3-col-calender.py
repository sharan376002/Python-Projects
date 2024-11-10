import calendar

cal = calendar.TextCalendar(calendar.SUNDAY)
#year 2024 col width 2 lin per weeek 1
# no of space btw month col : 1
# 3 : no of moonth per col
print(cal.formatyear(2024,3,1,5,4))