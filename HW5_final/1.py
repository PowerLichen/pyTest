"""
  Project: statistics student GPA
  Author: Minsu Choe
  StudentID: 21511796
  Date of last update: Apr. 5, 2021
"""

# calculate statistics and print function
def statistics_student_GPA(GPA_list):
    GPAs_min = min(GPA_list)
    GPAs_max = max(GPA_list)
    GPAs_avg = sum(GPA_list)/len(GPA_list)
        
    print("statistics_student_GPA ::")
    print(" - LGPAs = {}".format(GPA_list))
    print(" - num_students = {}".format(len(GPA_list)))
    print(" - Statistics of GPAs : Max ({}), Min({}), Avg({})".format(GPAs_max, GPAs_min, GPAs_avg))

# define student list
students = [
    ('Kim','EE', 12345, (2000,12,25), 4.0),
    ('Lee', 'ME', 11234, (2019,9,1),4.2),
    ('Park', 'ICE', 10234, (2019,3,1), 4.3),
    ('Hong', 'CE', 13123, (2021,1,1), 4.1),
    ('Yoon', 'ICE', 11321, (2001,8,15), 4.2),
    ('Choe', 'EE', 12321, (2000,7,31),4.2),
    ('Chung', 'CE', 18942, (2015,6,3), 4.0),
    ('Gang', 'CE', 11333, (2016,8,1), 3.8),
    ('Joe', 'ME', 12212, (2018,5,25), 3.9),
    ('Jang', 'EE', 14521, (2020,6,25), 4.4)
]

# print students
print("students =")
for i in students:
    print(i)

# make GPA list
GPAs=list(map(lambda x:x[4],students))

statistics_student_GPA(GPAs)

