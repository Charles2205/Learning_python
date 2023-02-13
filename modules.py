# # import random as rand
# # num =rand.shuffle(2,1)
# # print(num)

# import calendar
# year =2023
# print(calendar.calendar(year,m=1))

# # Assignment:Create a program to ask the user of the year and month of the calendar the user wants to see
import calendar as cal 

year=int(input('Enter the year you want to see: '))
month=int(input('Enter the month you want to see: '))
results=cal.calendar(year)

print(results)

# import datetime as dt
# print(dt.date.today())

