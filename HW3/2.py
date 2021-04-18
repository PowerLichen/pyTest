"""
  Project: Calculator bitwise
  Author: Minsu Choe
  StudentID: 21511796
  Date of last update: Mar. 21, 2021
"""
# input hex number
a = (int(input("hexadecimal a = "), base=16))
b = (int(input("hexadecimal b = "), base=16))

# print input value
print("a = {0} = {1}".format(hex(a), bin(a)))
print("b = {0} = {1}".format(hex(b), bin(b)))
# print bitwise calculated value
print("a & b = {0} = {1}".format(hex(a & b), bin(a & b)))
print("a | b = {0} = {1}".format(hex(a | b), bin(a | b)))
print("a ^ b = {0} = {1}".format(hex(a ^ b), bin(a ^ b)))
