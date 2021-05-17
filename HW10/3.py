"""
  Project: Homework 10.3
  Author: 최민수
  StudentID: 21511796
  Date of last update: May. 17, 2021
  Detail: 텍스트 파일에 저장된 7x7를 읽고 2차원 ndarray를 생성한 후
          역행렬을 계산하고, 해당 행렬과 역행렬의 곱을 출력
"""
import numpy as np

def loadtxt():
    arr = list()
    with open("array.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            arr.append(list(map(float, line.split())))
    return np.array(arr)

if __name__ == "__main__":
    A = loadtxt()
    A_inv = np.linalg.inv(A)
    E = np.matmul(A, A_inv)
    print("A =\n", A)
    print("A_inv =\n", A_inv)
    print("E = np.matmul(A, A_inv) =\n", E)