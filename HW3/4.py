"""
  Project: Print calender
  Author: Minsu Choe
  StudentID: 21511796
  Date of last update: Mar. 21, 2021
"""

# input datetime
str_datetime = input("input year month day : ")
dt_list = str_datetime.split(" ")

# cast str to int
year = int(dt_list[0])
month = int(dt_list[1])
day = int(dt_list[2])

count = 0

# define const array
month_str = ("", "January", "February", "March", "April", "May", "June",
             "July", "August", "September", "October", "November", "December")
count_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week_day = ("SUN", "MON", "TUE", "WED", "THR", "FRI", "SAT")


# set leap year
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    count_month[1] = 29


# count year
for i in range(1, year):
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        count+=366
    else:
        count+=365

# count month
for i in range(1, month):
    count += count_month[i-1]

# count increse 1 for week day
count+=1

# print month
print()
print("{} of Year {}".format(month_str[month], year))

print("="*4*7)

# print week
for i in week_day:
    print(" {}".format(i), end="")

print()
print("-"*4*7)

#print blank for calender
for i in range(count % 7):
    print("{:4}".format(""), end="")

#print calender
for i in range(1, count_month[month-1]+1):
    print("{:4}".format(i), end="")
    if count % 7 == 6:
        print()
    count += 1

print()
print("="*4*7)
