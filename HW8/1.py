"""
  Project: Homework 8.1
  Author: 최민수
  StudentID: 21511796
  Date of last update: May. 3, 2021
  Detail: 국가 데이터를 저장한 파일을 읽고 출력한 뒤, 인구 수 기준 내림차순
          으로 정렬하여 출력
"""

countries = []
# 데이터 읽기
with open('demography.txt','r') as f:
    for line in f:
        country, capital, population, area = line.split()
        countries.append((country,capital,int(population), int(area)))

# 기본 출력
print("List of countries")
for i in range(len(countries)):
    print("Country[{:2}] = {}".format(i,countries[i]))
print()

# 정렬 후 출력
countries.sort(key=lambda k:k[2],reverse=True)
print("List of countries sorted by demography(number of people) :")
for i in range(len(countries)):
    print("Country[{:2}] = {}".format(i,countries[i]))

