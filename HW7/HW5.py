"""
  Project: Homework 7.5
  Author: 최민수
  StudentID: 21511796
  Date of last update: Apr. 19, 2021
  Detail: 행렬 (matrix)의 덧셈, 뺄셈, 곱셈 연산을 연산자 오버로딩 기능으로 사용
          할 수 있게 하는 class Mtrx를 구현 생성자, 접근자, 변경자와 출력 함수를
          포함하여 구현
"""
class Mtrx:
    def __init__(self, name, n_row, n_col, L_data):
        self.name=name
        self.n_row=n_row
        self.n_col=n_col
        self.L_data=L_data
    def __str__(self):
        L_data = ["\n"]
        for i in range(self.n_row * self.n_col):
            L_data.append("{:2}".format(self.L_data[i]))
            if (i+1) % self.n_row == 0:
                L_data.append("\n")
        
        return " ".join(L_data)

    def __add__(self, other):
        result_data = []
        for i in range(len(self.L_data)):
            result_data.append(self.L_data[i] + other.L_data[i])
        return Mtrx("addMtrx",self.n_row, self.n_col, result_data)

    def __sub__(self, other):
        result_data = []
        for i in range(len(self.L_data)):
            result_data.append(self.L_data[i] - other.L_data[i])
        return Mtrx("subMtrx",self.n_row, self.n_col, result_data)
        
    def __mul__(self, other):
        result_data = []
        for i in range(self.n_col):
            for j in range(other.n_row):
                count=0
                for k in range(self.n_row):
                    count+=self.L_data[k+i*self.n_row] * other.L_data[k * other.n_row+j]
                result_data.append(count)

        return Mtrx("mulMtrx", other.n_row, self.n_col, result_data)

#‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐
if __name__ == "__main__":
    data_1 = [ 1, 2, 3, 4, 5,\
            6, 7, 8, 9, 10,\
            11, 12, 13, 14, 15,\
            16, 17, 18, 19, 20,\
            21, 22, 23, 24, 25]
    data_2 = [1, 0, 0, 0, 0,\
            0, 1, 0, 0, 0,\
            0, 0, 1, 0, 0,\
            0, 0, 0, 1, 0,\
            0, 0, 0, 0, 1]
    m1 = Mtrx("M1", 5, 5, data_1)
    print("m1 = ", m1)
    m2 = Mtrx("M2", 5, 5, data_2)
    print("m2 = ", m2)
    m3 = m1 + m2
    print("m3 = m1 + m2 =", m3)
    m4 = m1 - m2
    print("m4 = m1 ‐ m2 =", m4)
    m5 = m1 * m2
    print("m5 = m1 * m2 =", m5)