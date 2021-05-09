"""
  Project: Exam1C
  Author: 최민수
  StudentID: 21511796
  Date of last update: Apr. 24, 2021
  Detail: 피보나치 수열을 계산하는 myFibo.py 파일을 이용하여 출력
"""
import myFibo
print("2021-1 Exam1C 학번: 21511796, 성명: 최민수")

if __name__ == "__main__":
    # 반복 수행 시작
    while True:
        # mode 입력
        mode = input("Fibonacci series calculation mode (sr or dyn, q to quit) : ")
        # q일시 반복 종료
        if mode == "q":
            break
        # 간단한 재귀 피보나치 수열 실행
        if mode == "sr":
            start, stop, step = map(int,input("start, stop, strp fo Fibo calculation : ").split())
            for i in range(start,stop,step):
                print("{:3}-th Fibo series = {:25}".format(i,myFibo.srFibo(i)))
        # 동적 프로그래밍 피보나치 수열 실행
        if mode == "dyn":
            start, stop, step = map(int,input("start, stop, strp fo Fibo calculation : ").split())
            for i in range(start, stop, step):
                print("{:3}-th Fibo series = {:25}".format(i,myFibo.dynFibo(i)))