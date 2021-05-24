"""
  Project: Homework 11.3
  Author: 최민수
  StudentID: 21511796
  Date of last update: May. 23, 2021
  Detail: 세 가지 정렬함수를 구현하고 각각 걸리는 시간을 측정하여 비교
"""
import random
import time

def genRandList(L, size):
    for i in range(0, size):
        L.append(i)
    random.shuffle(L)

def selectionSort(arr, size):
    for i in range(0, size-1):
        min = i
        for j in range(i+1, size):
            if(arr[min] > arr[j]):
                min = j
        if (min!=i):
            arr[i], arr[min] = arr[min], arr[i]

def merge(L_left, L_right):
    result = []
    l = h = 0
    while l < len(L_left) and h < len(L_right):
        if L_left[l] < L_right[h]:
            result.append(L_left[l])
            l += 1
        else:
            result.append(L_right[h])
            h += 1
    result += L_left[l:]
    result += L_right[h:]    
    return result

def mergeSort(L):
    if len(L) < 2:
        return L
    else:
        mid = len(L) // 2
        L_left = mergeSort(L[:mid])
        L_right = mergeSort(L[mid:])
        return merge(L_left, L_right)

def _partition(arr, left, right, pi):
    pv = arr[pi]
    arr[pi], arr[right] = arr[right], arr[pi]
    new_pi = i = left
    while i <= (right - 1):
        if arr[i] <= pv:
            arr[new_pi], arr[i] = arr[i], arr[new_pi]
            new_pi += 1
        i += 1
    arr[new_pi], arr[right] = arr[right], arr[new_pi]
    return new_pi

def _quickSortLoop(arr, left, right):
    if(left >= right):
        return
    pi = (left + right) // 2
    new_pi = _partition(arr, left, right, pi)
    if left < (new_pi - 1):
        _quickSortLoop(arr, left, new_pi-1)
    if right > (new_pi + 1):
        _quickSortLoop(arr, new_pi+1, right)

def quickSort(L):
    size = len(L)
    _quickSortLoop(L, 0, size-1)


def printListSample(L, size, per_line, sample_line):
    max_line_count = per_line*sample_line   # 출력할 라인의 가로x세로
    loop_num = min(size,max_line_count)     # 현재 크기와 출력할 라인 크기 중 작은것을 선택

    line_count = 0                          # 라인의 개수를 확인할 변수
    for i in range(loop_num):
        print("{:7}".format(L[i]), end='')
        if (i+1) % per_line == 0:           # 가로에 출력된 숫자 개수가 per_line과 동일하다면
            line_count += 1                 # line_count를 증가시키고 개행
            print()

    print(". . . . . .")

    line_count = 0
    for i in range(loop_num):
        print("{:7}".format(L[size-loop_num+i]), end='')    # 뒤에서부터 출력해야 하므로 size에서
        if (i+1) % per_line == 0:                       # loop_num 앞의 위치에서부터 출력
            line_count += 1
            print()

def sortAndCompare(L, size):
    # 선택 정렬
    if(size <= 50000):
        temp_L = L
        print("Before Selection-Sort of A :")
        printListSample(temp_L, size, 10, 3)
        t1 = time.time()
        selectionSort(temp_L, size)
        t2 = time.time()
        print("After Selection-Sort of A :")
        printListSample(temp_L, size, 10, 3)
        print("Selection sorting took {} sec".format(t2-t1))
        print()
    
    # 병합 정렬
    temp_L = L
    print("Before mergeSort of A :")
    printListSample(temp_L, size, 10, 3)
    t1 = time.time()
    temp_L = mergeSort(temp_L)
    t2 = time.time()
    print("After mergeSort of A :")
    printListSample(temp_L, size, 10, 3)
    print("Merge sorting took {} sec".format(t2-t1))
    print()

    # 퀵 정렬
    temp_L = L
    print("Before quickSort of A :")
    printListSample(temp_L, size, 10, 3)
    t1 = time.time()
    quickSort(temp_L)
    t2 = time.time()
    print("After quickSort of A :")
    printListSample(temp_L, size, 10, 3)
    print("Quick sorting took {} sec".format(t2-t1))


def main():
    list_A = list()
    
    # 크기 입력
    print("Comparisons of sorting algorithms")
    size = int(input("Input array Size(-1) to quit = "))
    
    # 랜덤 리스트 생성
    genRandList(list_A, size)

    sortAndCompare(list_A, size)



if __name__ == "__main__":
    main()
    