"""
  Project: Student Information System by tuple
  Author: Minsu Choe
  StudentID: 21511796
  Date of last update: Mar. 29, 2021
"""

# define tuple list
L_students = []
L_students.append(("Kim, S.C.", 12001234, "CE", 4.10))
L_students.append(("Choi, Y.B.", 119003234, "EE", 3.78))
L_students.append(("Hong C.H ", 21001547, "ICE", 4.13))
L_students.append(("Yoon, J.H.", 17002571, "ME", 3.55))
L_students.append(("Lee, S.H.", 20003257, "ICE", 4.45))
L_students.append(("Kim H.Y.", 19001234, "CE", 4.17))
L_students.append(("Lee, J.K.", 18003234, "EE", 3.78))
L_students.append(("Park, S.Y.", 21001643, "ICE", 4.13))
L_students.append(("Jang, S.H.", 19002567, "ME", 3.35))
L_students.append(("Yeo, C.S.", 20005243, "CE", 4.45))

# print list
for i in range(len(L_students)):
    print("students[{:2}] : name({}), st_id({}), major({}, GPA({}))".format(
        i, L_students[i][0], L_students[i][1], L_students[i][2], L_students[i][3]))

# print normal sort
L_students.sort()
print("After sorting in increasing order :")
for i in range(len(L_students)):
    print("students[{:2}] : name({}), st_id({}), major({}, GPA({}))".format(
        i, L_students[i][0], L_students[i][1], L_students[i][2], L_students[i][3]))

# print sort order by GPA
L_students.sort(key= lambda x: x[3],reverse=True)
print("After sorting according to GPA in decreasing order :")
for i in range(len(L_students)):
    print("students[{:2}] : name({}), st_id({}), major({}, GPA({}))".format(
        i, L_students[i][0], L_students[i][1], L_students[i][2], L_students[i][3]))

