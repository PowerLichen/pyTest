"""
  Project: myFibo
  Author: 최민수
  StudentID: 21511796
  Date of last update: Apr. 24, 2021
  Detail: 간단한 재귀 피보나치 수열과 동적 프로그래밍 피보나치 구현
"""
# dict 자료형 선언
fibo_memo=dict()

# 간단한 재귀 피보나치
def srFibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n>1:
        return srFibo(n-1) + srFibo(n-2)

# 동적 프로그래밍 피보나치
def dynFibo(n):
    if n<2:
        fibo_memo[n]=n
        return n
    else:
        if fibo_memo.get(n) != None:
            return fibo_memo[n]
        else:
            fibo_memo[n] = dynFibo(n-2) + dynFibo(n-1)
            return fibo_memo[n]