# Area and Circumference of Circle
"""
  Project: Area and Circumference of Circle
  Author: Minsu Choe
  Date of last update: Mar. 12, 2021
"""

#define const value
PI = 3.141592

#define radius value
radius = int(input("input radius = "))

# calculate answer
area = radius * radius * PI
circumference = 2*radius*PI

# print answer
print("area:", area)
print("circumference:",circumference)