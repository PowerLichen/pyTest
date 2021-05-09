
"""
  Project: Exam1B
  Author: 최민수
  StudentID: 21511796
  Date of last update: Apr. 24, 2021
  Detail: 다각형의 꼭지점 개수, 중심좌표를 입력받고 선 길이가 100인 다각형을
          지정된 중심점에 그리는 함수를 작성
"""

import turtle
import math

def drawPolygon(t,num_vertices, center_x, center_y, line_length, color):
    # check polygon vertex number
    if num_vertices<3:
        return


    # initialize turtle
    t.color(color)
    t.width(3)

    # move to main coordinates
    t.up()
    t.goto((center_x,center_y))
    t.down()

    # draw dot and write (x,y) in main coordinates 
    t.dot(10,color)
    t.write(t.position())
    

    loop_count=0

    # set start coordinates
    if num_vertices % 2==0:
        # set start coordinates if even number
        start_x = center_x - line_length/2
        start_y = center_y + (line_length/2)/math.tan(math.radians(180/num_vertices))
        t.up()
        t.goto((start_x,start_y))
        t.down()
    else:
        # set start coordinates if odd number
        start_x = center_x
        start_y = center_y + line_length/2/math.sin(math.radians(180/num_vertices))
        t.up()
        t.goto((start_x,start_y))
        t.down()
        t.right(180/num_vertices)
    
    # draw line
    while loop_count<num_vertices:
        t.dot(10,"red")
        t.write(t.position())
        t.forward(line_length)
        t.right(360/num_vertices)
        loop_count+=1

    # reset turtle
    t.up()
    t.home()
    t.down()

# define turtle
t= turtle.Turtle()
turtle.title("2021-1 Exam1B 학번: 21511796, 성명: 최민수")

while True:
    num_vertices, center_x, center_y = map(int,\
        input("num_vertices center_x center_y: ").split())

    if num_vertices ==0:
        break

    drawPolygon(t,num_vertices,center_x, center_y, 100, "blue")






