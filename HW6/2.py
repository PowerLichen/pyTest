# User‐defined package/module
import sys
myPyPackage_dir = "C:/"
sys.path.append(myPyPackage_dir)

from MyPyPackage.myModules\
    import MyList, MySortings

L = []
n = 100

MyList.genRandList(L, n)
print("Before Sorting :")
MyList.printListSample(L, n, 10, 3)

MySortings.selectionSort(L)

print("\nAfter Sorting :")
MyList.printListSample(L, n, 10, 3)