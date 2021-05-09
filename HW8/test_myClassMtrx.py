"""
  Project: Homework 8.3 test_myClassMtrx.py
  Author: 최민수
  StudentID: 21511796
  Date of last update: May. 3, 2021
  Detail: 텍스트 파일에서 2개의 행렬 데이터를 읽어 계산하고, 결과를 출력
"""
from myClassMtrx import MyMtrx

def setMtrx(f, name):
    num_rows, num_cols = map(int, f.readline().split())
    list_data = []
    for i in range(num_cols):
        data = list(map(float, f.readline().split()))
        list_data +=data

    return MyMtrx(name,num_rows,num_cols, list_data)


if __name__ == "__main__":
    # 파일 열어서 배열에 저장
    with open('matrix_data.txt','r') as f:
        mA = setMtrx(f, "mA")
        print("n_rows: {}, n_cols: {}".format(mA.num_rows,mA.num_cols))
        print("mA = ")
        print(mA)

        mB = setMtrx(f, "mB")
        print("n_rows: {}, n_cols: {}".format(mB.num_rows,mB.num_cols))
        print("mB = ")
        print(mB)

    print("mC = mA + mB = ")
    print(mA + mB)
    print("mD = mA - mB = ")
    print(mA - mB)
    print("mE = mA x mB = ")
    print(mA * mB)

