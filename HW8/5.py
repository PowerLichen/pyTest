"""
  Project: Homework 8.5
  Author: 최민수
  StudentID: 21511796
  Date of last update: May. 3, 2021
  Detail: 엑셀 파일을 열고 학생 평균과 과목 평균을 추가한 뒤 출력하고
          엑셀 파일로 저장
"""
import pandas as pd
import numpy as np

# Excel 파일을 읽어 데이터 프레임을 생성
df = pd.read_excel('student_scores.xlsx')

# 학생들의 성적 평균을 계산하여 'Avg'열 추가
avgs_per_student = df.iloc[:,1:].mean(1)
df.loc[:, 'Avg'] = avgs_per_student

# 학생 성적 평균 기준으로 내림차순 정렬
df.sort_values(by='Avg', ascending=True)

# 각 과목을 평균을 계산하고 'Total_Avg'행 추가
avgs_per_class = df.mean()
df.loc[len(df)] = avgs_per_class
df.at[len(df)-1, 'st_id'] = None
df.at[len(df)-1, 'st_name'] = 'Total_Avg'

# 데이터 프레임 출력
print("df = \n", df)

# 데이터 프레임을 엑셀 파일로 출력
with pd.ExcelWriter("processed_scores.xlsx") as excel_writer:
    df.to_excel(excel_writer)