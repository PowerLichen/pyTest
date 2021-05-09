"""
  Project: Exam1D
  Author: 최민수
  StudentID: 21511796
  Date of last update: Apr. 24, 2021
  Detail: 두 도시의 거리를 구하는 함수들을 작성하고, main에서 사용하여 출력
"""

print("2021-1 Exam1D 학번: 21511796, 성명: 최민수")

# 두 도시와 거리를 입력받아 반환하는 함수
def getInterCityDist():
    city_1, city_2, str_dist = map(str,input("Input name of two cities and distance in Km: ").split())
    return city_1, city_2, int(str_dist)

# 인수로 전달받은 두 도시와 거리를 딕셔너리에 저장하는 함수
def setInterCityDist(dict_ICD, city_1, city_2, dist):
    dict_ICD[(city_1,city_2)] = dist

# 딕셔너리에서 두 도시로 된 key를 찾고 거리를 반환하는 함수
def findInterCityDist(dict_ICD, city_1, city_2):
    if (city_1, city_2) in dict_ICD:
        return dict_ICD[(city_1, city_2)]
    if (city_2, city_1) in dict_ICD:
        return dict_ICD[(city_2, city_1)]
    return None


if __name__ == "__main__":
    interCityDist = dict()
    # 5개의 도시 이름 쌍과 거리를 입력받는 반복문
    for i in range(5):
        city_1, city_2, dist = getInterCityDist()
        setInterCityDist(interCityDist, city_1, city_2, dist)
    
    # 딕셔너리 출력
    print("Inter_City_Distance_Table : {}".format(interCityDist))

    # 도시 찾기 반복문
    while True:
        city_1, city_2 = map(str, input("Input name of two cities to find distance : ").split())
        # 둘 중 하나라도 "."일 경우, 반복문 종료
        if city_1 == "." or city_2 == ".":
            break
        
        dist = findInterCityDist(interCityDist, city_1, city_2)
        print("Distance between ({} - {}) is ".format(city_1,city_2), end="")
        
        # 찾지 못한 경우 데이터가 없다는 문자열 출력
        if dist == None:
            print("not defined yet")
        else:
            print("{} Km.".format(dist))