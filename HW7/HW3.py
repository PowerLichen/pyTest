"""
  Project: Homework 7.3
  Author: 최민수
  StudentID: 21511796
  Date of last update: Apr. 19, 2021
  Detail: Date 클래스를 생성자, 접근자, 변경자와 출력 함수를 포함하여 구현
"""
import random
class Date:
    def __init__(self, yr, mt, dy):
        self.setYear(yr)
        self.setMonth(mt)
        self.setDay(dy)
    def __lt__(self,other):
        if (self.yr, self.mt, self.dy)\
            < (other.yr, other.mt, other.dy):
            return True
        else:
            return False
    def __str__(self):
        return "({:4}-{:2}-{:2})".format(self.yr, self.mt, self.dy)
    def getYear(self):
        return self.yr
    def getMonth(self):
        return self.mt
    def getDay(self):
        return self.dy
    def setYear(self,yr):
        self.yr=yr
    def setMonth(self,mt):
        if mt<1 or mt>12:
            print("*** Error in setting month (Year:{}, month:{})".\
                format(self.yr, mt))
            mt=1
        self.mt=mt
    def setDay(self,dy):
        month_day = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        year=self.yr
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            month_day[2]=29
        if dy<1 or dy>month_day[self.mt]:
            print("*** Error in setting day (year:{}, month:{}, day:{})".\
                format(self.yr, self.mt, dy))
            dy=1
        self.dy=dy


######################################################
# Application
#‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐
if __name__ == "__main__":
    dates = [ ]
    for i in range(10):
        date = Date(random.randrange(1900,2022), random.randrange(0,13), random.randrange(0,32))
        dates.append(date)
    print("dates before sorting : ")
    for d in dates:
        print(d)
    #
    dates.sort()
    print("\nstudents after sorting : ")
    for d in dates:
        print(d)