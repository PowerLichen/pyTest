
"""
  Project: Exam1A
  Author: 최민수
  StudentID: 21511796
  Date of last update: Apr. 24, 2021
  Detail: 실수 데이터 리스트를 입력받고 저장한 후, 입력된 실수형 데이터 중
          최소값, 최대값, 평균값, 분산, 표준편차를 계산하여 출력
"""

print("2021-1 Exam1A 학번: 21511796, 성명: 최민수")

# 실수 데이터 리스트 입력
data_list = list(map(float,input("input 10 float data: ").split()))
print("list of input data: {}".format(data_list))

L_min = data_list[0]
L_max = data_list[0]
L_sum = 0.0
L_len = len(data_list)

# 최대, 최소, 평균 계산
for num in data_list:
    L_sum += num
    if num < L_min:
        L_min = num
    if num > L_max:
        L_max = num

L_avg = L_sum / L_len

# 분산과 표준편차 계산
L_sum = 0.0
for num in data_list:
    temp = num - L_avg
    L_sum += temp ** 2

L_var = L_sum / L_len
L_std = L_var ** (1/2)

#결과 출력
print("L_min = {}, L_max = {}, L_avg = {}, L_var = {}, L_std = {}".\
    format(L_min, L_max, L_avg, L_var, L_std))