"""
  Project: Matrix calculator
  Author: Minsu Choe
  StudentID: 21511796
  Date of last update: Apr. 5, 2021
"""
# print matrix
def printMtrx(name, M):
    print("{} = ".format(name))
    for i in M:
        for j in i:
            print("{:3}".format(j),end="")
        print()
    print()

# Add function
def matrixAdd(A,B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return None
    result =[ [0]* len(A[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j]=A[i][j]+B[i][j]
    return result

# Subtract function
def matrixSubtract(A,B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return None
    result =[ [0]* len(A[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j]=A[i][j]-B[i][j]
    return result

# Multiply function
def matrixMultiply(A,B):
    if len(A[0]) != len(B):
        return None
    result =[ [0]* len(A) for i in range(len(B[0]))]

    for i in range(len(result)):
        for j in range(len(result[0])):
            for k in range(len(A[0])):
                result[i][j] += A[i][k]*B[k][j]

    return result



# define two matrix
A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

printMtrx("A",A)
printMtrx("B",B)

C = matrixAdd(A,B)
printMtrx("A+B",C)

D = matrixSubtract(A,B)
printMtrx("A-B",D)

E = matrixMultiply(A,B)
printMtrx("A*B",E)