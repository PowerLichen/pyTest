"""
  Project: Homework 8.2
  Author: 최민수
  StudentID: 21511796
  Date of last update: May. 3, 2021
  Detail: 학생 정보 데이터를 저장한 파일을 읽고 평균 점수와 과목별 
          평균점수를 계산한 뒤 결과를 output.txt로 출력
"""
student_file = []

f = open('student_records.txt','r')
# 파일 읽기
for line in f:
    name, kor, eng, math, sci = line.split()
    temp = [name, int(kor), int(eng), int(math), int(sci)]
    student_file.append(temp)
f.close()

# 학생별 평균점수를 계산하여 추가
i=0
for name, kor, eng, math, sci in student_file:
    sum = kor + eng + math + sci
    avg = sum/4.0
    student_file[i].append(avg)
    i = i + 1


# 각 과목별 성적 종합
Kor_avg, Eng_avg, Math_avg, Sci_avg = 0, 0, 0, 0
length = len(student_file)
for name, kor, eng, math, sci, avg in student_file:
    Kor_avg +=kor
    Eng_avg +=eng
    Math_avg += math
    Sci_avg +=sci
Kor_avg /= length
Eng_avg /= length
Math_avg /= length
Sci_avg /= length

# 텍스트 파일 출력
with open('output.txt','w') as f:
    f.write("{:<5} : {:>5}, {:>5}, {:>5}, {:>5}, {:>6}\n".\
        format("name","kor", "eng","math","sci","avg"))
    f.write("=============================================\n")
    for i in range(len(student_file)):
        s = "{:<5} : {:5}, {:5}, {:5}, {:5}, {:>6.2f}\n".\
            format(student_file[i][0], student_file[i][1], student_file[i][2], student_file[i][3], student_file[i][4], student_file[i][5])
        f.write(s)
    f.write("\n{:<5} : {:5}, {:5}, {:5}, {:5}, {:}".\
        format("Avg",Kor_avg,Eng_avg,Math_avg,Sci_avg,""))
    


