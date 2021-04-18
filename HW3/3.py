"""
  Project: Calculate elapsed date
  Author: Minsu Choe
  StudentID: 21511796
  Date of last update: Mar. 21, 2021
"""

# define const array
week_day = ("MON", "TUE", "WED", "THR", "FRI", "SAT", "SUN")
count_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

str_datetime = ""

while True:
    # input datatime
    str_datetime = input("input year month day : ")
    dt_list = str_datetime.split(" ")

    # cast str to int
    year = int(dt_list[0])
    month = int(dt_list[1])
    day = int(dt_list[2])

    count = 0

    # count year
    for i in range(1, year):
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            count += 366
        else:
            count += 365

    # count month
    for i in range(1, month):
        count += count_month[i-1]

    # count day
    count += day

    # print input string
    print("Input tr_mn_dy_strings : {}".format(dt_list))

    # if input str is "0 0 0", break loop
    if(str_datetime == "0 0 0"):
        break
    # print date and week day, count value
    print("Day (year({0}), month({1}), day({2})) : ".format(
        dt_list[0], dt_list[1], dt_list[2]), end=' ')
    print("week_day({0}), elapsed {1} days from Jan01AD01".format(
        week_day[(count-1) % 7], count))
