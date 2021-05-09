"""
  Project: Exam1E
  Author: 최민수
  StudentID: 21511796
  Date of last update: Apr. 24, 2021
  Detail: 행렬의 생성 및 연산을 할 수 있는 class를 구현하고
          계산한 것을 출력
"""

class Mtrx: 
    def __init__(self, name, n_row, n_col, lst_data):
        self.name = name
        self.n_row = n_row
        self.n_col = n_col
        self.lst_data = lst_data

    # 출력 오버로딩
    def  __str__(self):
        lst_data = []
        # 리스트에 데이터를 추가
        for i in range(self.n_row * self.n_col):
            lst_data.append("{:3}".format(self.lst_data[i]))
            # 행만큼 추가된 경우, 강제개행 문자를 리스트에 추가
            if (i+1) % self.n_row == 0:
                lst_data.append("\n")
        # 리스트를 문자열 변환하여 반환
        return "".join(lst_data)
    
    # 덧셈 연산 오버로딩
    def __add__(self, other):
        result_data = []
        for i in range(len(self.lst_data)):
            result_data.append(self.lst_data[i] + other.lst_data[i])
        return Mtrx("addMtrx",self.n_row, self.n_col, result_data)
    
    # 뺄셈 연산 오버로딩
    def __sub__(self, other):
        result_data = []
        for i in range(len(self.lst_data)):
            result_data.append(self.lst_data[i] - other.lst_data[i])
        return Mtrx("subMtrx",self.n_row, self.n_col, result_data)
    
    # 곱셈 연산 오버로딩
    def __mul__(self, other):
        result_data = []
        for i in range(self.n_col):
            for j in range(other.n_row):
                count=0
                for k in range(self.n_row):
                    count+=self.lst_data[k + i*self.n_row] * other.lst_data[k*other.n_row + j]
                result_data.append(count)

        return Mtrx("mulMtrx", other.n_row, self.n_col, result_data)


if __name__ == "__main__":
    print("2021-1 Exam1E 학번: 21511796, 성명: 최민수")
    data1_3x4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    data2_3x4 = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0]
    data3_4x3 = [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0]
    

    M1 = Mtrx("M1",4,3,data1_3x4)
    M2 = Mtrx("M2",4,3,data2_3x4)
    M3 = Mtrx("M3",3,4,data3_4x3)

    print("M1 = \n{}".format(M1))
    print("M2 = \n{}".format(M2))
    print("M3 = \n{}".format(M3))

    M4 = M1 + M2
    M5 = M1 - M2
    M6 = M1 * M3

    print("M4 = M1 + M2 = \n{}".format(M4))
    print("M5 = M1 - M2 = \n{}".format(M5))
    print("M6 = M1 * M3 = \n{}".format(M6))

