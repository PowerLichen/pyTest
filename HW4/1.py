"""
  Project: Print ASCII list
  Author: Minsu Choe
  StudentID: 21511796
  Date of last update: Mar. 29, 2021
"""

#define list
upper_alp = [chr(i) for i in range(ord('A'),ord('Z')+1)]
lower_alp = [chr(i) for i in range(ord('a'),ord('z')+1)]
digits =  [chr(i) for i in range(ord('0'),ord('9')+1)]

#print list
print("Upper case alphabets :")
print(upper_alp)
print("Lower case alphabets :")
print(lower_alp)
print("Digits :")
print(digits)