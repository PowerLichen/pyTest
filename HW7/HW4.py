"""
  Project: Homework 7.4
  Author: 최민수
  StudentID: 21511796
  Date of last update: Apr. 19, 2021
  Detail: Time 클래스를 생성자, 접근자, 변경자와 출력 함수를 포함하여 구현
"""
import random
class Time:
    def __init__(self, hr, mn, sec):
        self.setHour(hr)
        self.setMinute(mn)
        self.setSecond(sec)
    def __lt__(self, other):
        if (self.hr, self.mn, self.sec)\
            <(other.hr, self.mn, self.sec):
            return True
        else:
            return False
    def __str__(self):
        return "({:2}:{:2}:{:2})".format(self.hr, self.mn, self.sec)
    def getHour(self):
        return self.hr
    def getMinute(self):
        return self.mn
    def getSecond(self):
        return self.sec
    def setHour(self,hr):
        if hr<0 or hr>=24:
            print("*** Error in setting Hour (Hour:{})".\
                format(hr))
            hr=0
        self.hr=hr
    def setMinute(self, mn):
        if mn<0 or mn>=60:
            print("*** Error in setting Minute (Minute:{})".\
                format(mn))
            mn=0
        self.mn=mn
    def setSecond(self, sec):
        if sec<0 or sec>=60:
            print("*** Error in setting Second (Second:{})".\
                format(sec))
            sec=0
        self.sec=sec


######################################################
# Application
if __name__ == "__main__":
    times = []
    for i in range(10):
        time = Time(random.randrange(0,25), random.randrange(0,65), random.randrange(0,65))
        times.append(time)

    print("times before sorting : ")
    for t in times:
        print(t)
    #
    times.sort()
    print("\ntimes after sorting : ")
    for t in times:
        print(t)