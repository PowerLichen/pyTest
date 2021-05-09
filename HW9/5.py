"""
  Project: Homework 9.5
  Author: 최민수
  StudentID: 21511796
  Date of last update: May. 9, 2021
  Detail: 테이블 위에서 공이 벽면에 반사되며 이동하는 시뮬레이션
          기능을 파이썬 tkinter 그래픽 프로그램으로 구현
"""

from tkinter import *
from tkinter import messagebox

# 화면 종료 이벤트
def ask_quit():
    result = messagebox.askquestion("Message", "Quit")
    if result == "yes":
        window.destroy()

# 키보드 입력 이벤트
def change_direction(event):
    global DX, DY
    
    if event.keysym == "Left":
        DX = -STEP; DY = 0
        print("input key : Left")
    elif event.keysym == "Right":
        DX = STEP; DY = 0
        print("input key : Right")
    elif event.keysym == "Up":
        DX = 0; DY = -STEP
        print("input key : Up")
    elif event.keysym == "Down":
        DX = 0; DY = STEP
        print("input key : Down")
    elif event.keysym == "Escape":
        DX = STEP; DY = STEP
        print("input key : ESC")
    else:
        DX = STEP; DY = STEP
        
# 윈도우 초기 설정
def init():
    global window, canvas, DX, DY, STEP
    # 화면 초기 설정
    window = Tk()
    window.title("Ball animation")
    canvas = Canvas(window, width=600, height=400)
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_oval(0, 0, 80, 80, fill="red", tags="myBall")
    STEP = 1
    DX = STEP
    DY = STEP
    # 키입력 이벤트 설정
    window.protocol("WM_DELETE_WINDOW", ask_quit)
    window.bind("<KeyPress-Left>", change_direction)
    window.bind("<KeyPress-Right>", change_direction)
    window.bind("<KeyPress-Up>", change_direction)
    window.bind("<KeyPress-Down>", change_direction)
    window.bind("<KeyPress-Escape>", change_direction)

# 애니메이션 설정
def animate():
    global DX, DY
    delay = 10
    canvas.move("myBall", DX, DY)
    pos = canvas.coords("myBall")
    if pos[0] <0 or pos[2] > canvas.winfo_width():
        DX *= -1
    if pos[1]< 0 or pos[3] > canvas.winfo_height():
        DY *= -1
    canvas.update_idletasks()
    canvas.update()
    canvas.after(delay, animate)

if __name__ == '__main__':
    init()
    animate()
    mainloop()
