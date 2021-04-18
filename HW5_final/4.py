"""
  Project: draw polygon
  Author: Minsu Choe
  StudentID: 21511796
  Date of last update: Apr. 5, 2021
"""
import time

# define global list
fibo_memo=list()

# dynamic Fibonacci function
def dynFibo(n):
    if n < 0:
        return None
    elif 0 <= n < 2:
        fibo_memo[n]=n
        return n
    if(fibo_memo[n] != 0):
        # if memo has calculated num
        return fibo_memo[n]
    else:
        # if memo has not calculated num
        fibo_memo[n] = dynFibo(n-2) + dynFibo(n-1)
        return fibo_memo[n]

# add 0 number to memo = memo[0]
fibo_memo.append(0)

#input arguments
start, end, stride = map(int, input("input start, stop, step of Fibonacci series : ").split())

# resizing memo
for i in range(end):
    fibo_memo.append(0)

# print fibonacci number and elapsed time
for n in range(start,end+1,stride):
    start_t = time.time() * 1000
    result = dynFibo(n)
    end_t = time.time() * 1000
    print("dynFibo({:3}) = {:25}, took {:12}[milli_sec]".format(n,result,end_t-start_t))

