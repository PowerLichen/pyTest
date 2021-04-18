"""
  Project: Homework 7.2
  Author: 최민수
  StudentID: 21511796
  Date of last update: Apr. 19, 2021
  Detail: Student 생성자, 접근자, 변경자와 출력 함수를 포함하여 구현
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


class Student(Person):
    # define initiator
    def __init__(self, name, reg_id, age,st_id,major,GPA):
        super().__init__(name, reg_id, age)
        self.setStudentID(st_id)
        self.setMajor(major)
        self.setGPA(GPA)
    # define accessor
    def getStudentID(self,st_id):
        self.st_id=st_id
    def getMajor(self,major):
        self.major=major
    def getGPA(self,GPA):
        self.GPA=GPA

    # define mutator
    def setStudentID(self,st_id):
        if st_id<0:
            print("*** Error in setting StudentID (name:{}, StudentID:{})".format(self.name,st_id))
            st_id=0
        self.st_id=st_id
    def setMajor(self,major):
        if str(type(major)) != "<class 'str'>":
            print("*** Error in setting Major (name:{}, Major:{})".format(self.name,major))
            name="NoMajor"
        self.major=major
    def setGPA(self,GPA):
        if GPA<0.0 or GPA>4.5:
            print("*** Error in setting GPA (name:{}, GPA:{})".format(self.name,GPA))
            GPA = 0.0
        self.GPA=GPA
    def __str__(self):
        return "Student({}, {}, {}, {}, {}, {})".\
            format(self.name,self.reg_id,self.age,self.st_id,self.major,self.GPA)

def compareStudent(st1, st2, compare):
    if compare == "st_id":
        if st1.st_id < st2.st_id:
            return True
        else:
            return False
    if compare == "name":
        if st1.name < st2.name:
            return True
        else:
            return False
    if compare == "GPA":
        if st1.GPA > st2.GPA:
            return True
        else:
            return False

def sortStudent(L_st, compare):
    for i in range(0, len(L_st)):
        min_idx = i
        for j in range(i+1, len(L_st)):
            if compareStudent(L_st[j], L_st[min_idx], compare):
                min_idx = j
        if min_idx != i:
            L_st[i], L_st[min_idx] = L_st[min_idx], L_st[i]

def printStudents(L_st):
    for s in range(len(L_st)):
        print(L_st[s])
    

#Example of class Person, class Student inheritance in Python (2)
############################################
##########
# Application
if __name__ == "__main__":
    students = [
        Student("Kim", 990101, 21, 12345, "EE", 4.0),
        Student("Lee", 980715, 22, 11234, "ME", 4.2),
        Student("Park", 101225, 20, 10234, "ICE", 4.3),
        Student("Hong", 110315, 19, 13123, "CE", 4.1),
        Student("Yoon", 971005, 23, 11321, "ICE", 4.2),
        Student('Choe', 200120, 21, 12321, 'EE',4.2),
        Student('Chung',990111, 22 , 18942,'CE', 4.0),
        Student('Gang', 950730, 25 , 11333,'CE', 3.8),
        Student('Joe', 880505, 30, 12212, 'ME', 3.9),
        Student('Jang', 981223, 24, 14521,'EE', 4.4)
    ]
    print("students before sorting : ")
    printStudents(students)
    #
    sortStudent(students, "name")
    print("\nstudents after sorting by name : ")
    printStudents(students)
    #
    sortStudent(students, "st_id")
    print("\nstudents after sorting by student_id : ")
    printStudents(students)
    #
    sortStudent(students, "GPA")
    print("\nstudents after sorting by GPA in decreasing order : ")
    printStudents(students)