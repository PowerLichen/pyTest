"""
  Project: Homework 9.2
  Author: 최민수
  StudentID: 21511796
  Date of last update: May. 9, 2021
  Detail: 마우스 이벤트를 사용하여 캔버스에 버튼을 클릭하면 선을 출력
"""

import turtle

# 터틀 초기설정
board = turtle.Screen()
board.screensize(800, 600, 'light blue')

pointer = turtle.Turtle()
pointer.color('red')
pointer.pencolor('red')
pointer.ht()

# 마우스 왼쪽 클릭 이벤트
def teleport_btn1(x, y):
    pointer.pencolor('red')
    pointer.goto(x,y)
    pointer.write((pointer.xcor(), pointer.ycor()))

# 마우스 오른쪽 클릭 이벤트
def teleport_btn3(x,y):
    pointer.pencolor('blue')
    pointer.goto(x,y)
    pointer.write((pointer.xcor(), pointer.ycor()))

# 종료 이벤트
def quitThis():
    board.bye()

# 이벤트 지정
board.onclick(teleport_btn1, btn=1)
board.onclick(teleport_btn3, btn=3)
board.onkey(quitThis,'q')

# 터틀 스크린 시작
board.listen()
board.mainloop()