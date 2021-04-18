"""
  Project: Sort and measure elapsed time of integer list
  Author: Minsu Choe
  StudentID: 21511796
  Date of last update: Apr. 5, 2021
"""

import random
import time

# generate random number
def genBigRandList(L,n):
    # set list to non-repeating random numbers
    L=random.sample(range(n),n)
    return L

# print head 20 number and tail 20 number
def printListSample(L, per_line, sample_line):
    # print head 20 number
    for i in L[:20]:
        print("{:7} ".format(i), end="")
        if i==L[9]:
            print()
    print()
    print(". . . . . .")
    # print tail 20 number
    for i in L[-20:]:
        print("{:7} ".format(i), end="")
        if i==L[-11]:
            print()
    print()

# merge two list
def merge(left, right):
    #initialize var
    result = []
    l = h = 0
    # merge two list
    while l<len(left) and h<len(right):
        if left[l]<right[h]:
            result.append(left[l])
            l+=1
        else:
            result.append(right[h])
            h+=1
    result+=left[l:]
    result+=right[h:]    
    return result

# merge sort
def mergeSort(L):
    if len(L)<2:
        return L
    mid = len(L)//2
    left_L = L[:mid]
    right_L = L[mid:]
    left_L = mergeSort(left_L)
    right_L = mergeSort(right_L)
    return merge(left_L,right_L)





# input list size
list_size = int(input("Input size of random list L(-1 to quit) = "))
print()

# initialize list
L = list()

# generate rnad list
L=genBigRandList(L,list_size)

# print List
print("Before mergeSort of L :")
printListSample(L,10,2)

# measure start time
start = time.time()
# sort function
L = mergeSort(L)
# mesure end time
end = time.time()

# print List
print("After mergeSort of L :")
printListSample(L,10,2)

# print elapsed time
print("mergeSort() for list L (size = {}) took {} sec".format(list_size, end-start))
