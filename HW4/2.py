"""
  Project: Print sorted date-tuples
  Author: Minsu Choe
  StudentID: 21511796
  Date of last update: Mar. 29, 2021
"""

# define list
L_dates=[]

print("Input 10 times in (tear month day)format :")

# append input data to list
for i in range(10):
    raw_str = input("Input year, month, day : ")
    L_str_date = raw_str.split(sep=' ')
    L_dates.append(tuple(list(map(int,L_str_date))))
    print("L_dates = {}".format(L_dates))

# print before sorted list
print("After input of 10 dates : ")
print(L_dates)

# sort list
L_dates.sort(key= lambda x:x[2])
L_dates.sort(key= lambda x:x[1])
L_dates.sort(key= lambda x:x[0])

# print after sorted list
print("After sorting, L_dates = {}".format(L_dates))