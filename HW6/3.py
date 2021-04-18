# Comparison of List and Array with user‐defined modules (part 1)

import random, time, sys
from array import *
sys.path.append("C:/")
from MyPyPackage.myModules import MyList, MySortings

AR = array('i')
L = []
size = 50000
MyList.genRandList(L, size)

for x in L:
    AR.append(x)

# Comparison of List and Array with user‐defined modules (part 2)
print("Array (size : {}) before sorting : ".format(size))
MyList.printListSample(AR, size, 10, 2)
t1 = time.time()
MySortings.selectionSort(AR)
t2 = time.time()
print("Array (size : {}) after sorting : ".format(size))
MyList.printListSample(AR, size, 10, 2)
print("Selection sorting for array of {} integers took {} sec"\
    .format(size, t2-t1))

print("\nList (size : {}) before sorting : ".format(size))
MyList.printListSample(L, size, 10, 2)
t1 = time.time()
MySortings.selectionSort(L)
t2 = time.time()
print("\nList (size : {}) after sorting : ".format(size))
MyList.printListSample(L, size, 10, 2)
print("Selection sorting for list of {} integers took {} sec"\
    .format(size, t2-t1))