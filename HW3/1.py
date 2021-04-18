"""
  Project: Print Multiplication table
  Author: Minsu Choe
  StudentID: 21511796
  Date of last update: Mar. 21, 2021
"""

num = 12
num+=1

for i in range(1,num):
    for j in range(1,num):
        print("{:2} x {:2} = {:3},".format(i,j,i*j),end=" ")
    print()