"""
  Project: Homework 10.2
  Author: 최민수
  StudentID: 21511796
  Date of last update: May. 17, 2021
  Detail: 직병렬 전자회로의 선형시스템 해(solution)를 NumPy 선형대수
          유니버설 함수 solve()를 사용하여 구하라.
"""

import numpy as np

A = np.array([
    [10, 10, 0, 0, 0],
    [1, -1, -1, 0, 0],
    [0, 0, 1, -1, -1],
    [0, 10, -5, -10, 0],
    [0, 0, 0, 10, -10]
])
B = np.array([100,0,0,0,0])
X = np.linalg.solve(A,B)

print("A =\n", A)
print("B = ", B)
print("X = ", X)

print("np.matmul(A, X) = ", np.matmul(A,X))