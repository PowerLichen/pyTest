"""
  Project: Print sorted time-tuples
  Author: Minsu Choe
  StudentID: 21511796
  Date of last update: Mar. 29, 2021
"""

# define list
L_times=[]

print("Input 10 times in (hour minute sec) format :")

# append input data to list
for i in range(10):
    raw_str = input("Input hour minute second : ")
    L_str_time = raw_str.split(sep=' ')
    L_times.append(tuple(list(map(int,L_str_time))))
    print("L_times = {}".format(L_times))

# print before sorted list
print("After input of 10 times : ")
print(L_times)

# sort list
L_times.sort(key= lambda x:x[2])
L_times.sort(key= lambda x:x[1])
L_times.sort(key= lambda x:x[0])

# print after sorted list
print("After sorting, L_times = {}".format(L_times))