"""
  Project: Calculate elapsed and remain time
  Author: Minsu Choe
  StudentID: 21511796
  Date of last update: Mar. 21, 2021
"""


# input time
time_str = input("input hour min sec : ")
time_list = time_str.split(" ")

# convert input message to integer
hour = int(time_list[0])
minute = int(time_list[1])
second = int(time_list[2])

# calcurate time
elapsed = hour*3600 + minute*60 + second
remain = 86400-elapsed

# print elapsed time
print("Elapsed seconds from last midnight = {:02}:{:02}:{:02}".format(
    hour, minute, second))
# print remain time
print("Remaining seconds to next-midnight = {:02}:{:02}:{:02}".format(
    remain//3600, remain % 3600//60, remain % 3600 % 60))
