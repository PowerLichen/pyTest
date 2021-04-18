"""
  Project: Homework 7.1
  Author: 최민수
  StudentID: 21511796
  Date of last update: Apr. 19, 2021
  Detail: Person 클래스를 생성자, 접근자, 변경자와 출력 함수를 포함하여 구현
"""

class Person:
    # define initiator
    def __init__(self,name,reg_id,age):
        self.setName(name)
        self.setRegId(reg_id)
        self.setAge(age)
    
    # define accessor
    def getName(self):
        return self.name
    def getRegId(self):
        return self.reg_id
    def getAge(self):
        return self.age
    
    # define mutator    
    def setName(self, name):
        if str(type(name)) != "<class 'str'>":
            name="NoName"
        self.name = name
    def setRegId(self, reg_id):
        if reg_id>999999:
            print("*** Error in setting Reg Id (name:{}, RegId:{})".format(self.name,reg_id))
            reg_id=0            
        self.reg_id =reg_id
    def setAge(self, age):        
        if age<1 or age>150:
            print("*** Error in setting age (name:{}, age:{})".format(self.name,age))
            age=0
        self.age=age
    
    def __str__(self):
        s = "Person(\"{}\",{},{})".format(self.name,self.reg_id,self.age)
        return s



def printPersonList(L_persons):
    for p in L_persons:
        print(" ", p)
######################################################
# Application
if __name__ == "__main__":
    persons = [
        Person("Kim", 990101, 21),
        Person("Lee", 980715, 22),
        Person("Park", 101225, 20),
        Person("Hong", 110315, 19),
        Person("Yoon", 971005, 23),
        Person("Wrong", 100000, 350)
    ]
    print("persons : ")
    printPersonList(persons)