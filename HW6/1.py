# User‐defined package/module
import sys
myPyPackage_dir = "C:/"
sys.path.append(myPyPackage_dir)

from MyPyPackage.myModules import MyList

L = []
n = 50

MyList.genRandList(L, n)
MyList.printListSample(L, n, 10, 5)