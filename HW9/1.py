"""
  Project: Homework 9.1
  Author: 최민수
  StudentID: 21511796
  Date of last update: May. 9, 2021
  Detail: 다각형을 그리기 위한 튜플 리스트를 이용하여 그림 그리기
"""

import turtle

turtle.title("Drawing polygons with turtle.circle")
t = turtle.Turtle()

radius = 50

# 튜플 (radius, num_vertices, center_x, center_y, color) 리스트 정의
L_polygons = [
    (radius, 3, -255,100,"red"),
    (radius, 4, -75,100,"blue"),
    (radius, 5, 75,100,"green"),
    (radius, 6, 255,100,"magenta"),
    (radius, 7, -255,-100,"brown"),
    (radius, 8, -75,-100,"chocolate"),
    (radius, 9, 75,-100,"black"),
    (radius, 10, 255,-100,"indigo"),
]

for i in range(len(L_polygons)):
    radius, num_vertices, center_x, center_y, color = L_polygons[i]
    # 중심을 찍고 좌표값 출력
    t.up()
    t.goto(center_x, center_y)
    t.write(t.pos())
    t.down()
    t.dot(10, "red")

    # 다각형 그리기
    t.up()
    t.goto(center_x, center_y + radius)
    t.setheading(180)
    t.down()
    t.color(color)
    t.circle(radius, steps=num_vertices)


