"""
  Project: Homework 8.3 myClassMtrx.py
  Author: 최민수
  StudentID: 21511796
  Date of last update: May. 3, 2021
  Detail: 행렬의 초기화와 덧셈, 뺄셈, 곱셈, 출력 기능을 메소드로 가지는 
          MyMtrx 클래스를 작성
"""

class MyMtrx:
    # 초기화
    def __init__(self, name, num_rows, num_cols, list_data):
        self.name = name
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.list_data = list_data
    # 출력
    def __str__(self):
        lst_data = []
        # 리스트에 데이터를 추가
        for i in range(self.num_rows * self.num_cols):
            lst_data.append("{:5.1f}".format(self.list_data[i]))
            # 행만큼 추가된 경우, 강제개행 문자를 리스트에 추가
            if (i+1) % self.num_rows == 0:
                lst_data.append("\n")
        # 리스트를 문자열 변환하여 반환
        return "".join(lst_data)
    
    # 덧셈 연산 오버로딩
    def __add__(self, other):
        result_data = []
        for i in range(len(self.list_data)):
            result_data.append(self.list_data[i] + other.list_data[i])
        return MyMtrx("addMtrx",self.num_rows, self.num_cols, result_data)
    
    # 뺄셈 연산 오버로딩
    def __sub__(self, other):
        result_data = []
        for i in range(len(self.list_data)):
            result_data.append(self.list_data[i] - other.list_data[i])
        return MyMtrx("subMtrx",self.num_rows, self.num_cols, result_data)
    
    # 곱셈 연산 오버로딩
    def __mul__(self, other):
        result_data = []
        for i in range(self.num_cols):
            for j in range(other.num_rows):
                count=0
                for k in range(self.num_rows):
                    count+=self.list_data[k + i*self.num_rows] * other.list_data[k*other.num_rows + j]
                result_data.append(count)

        return MyMtrx("mulMtrx", other.num_rows, self.num_cols, result_data)