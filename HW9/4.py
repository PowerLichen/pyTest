"""
  Project: Homework 9.4
  Author: 최민수
  StudentID: 21511796
  Date of last update: May. 9, 2021
  Detail: Start, Pause, Reset 버튼를 가지는 스톱워치를 tkinter GUI 프로그램으로 구현
"""

import time
from tkinter import *

running = False

# 실시간 시간 체크 이벤트
def runTimer():
    global start_time, elapsed_time, prev_elapsed_time
    if(running):
        cur_time = time.time()
        time_diff = cur_time - start_time
        elapsed_time = time_diff + prev_elapsed_time
        timeText.configure(text="{:7.3f}".format(elapsed_time))
    window.after(10, runTimer)
# 시간측정 시작 이벤트
def start():
    global running, start_time, elapsed_time, prev_elapsed_time
    if(running!= True):
        running = True
        start_time = time.time()
        prev_elapsed_time = elapsed_time
# 시간측정 일시중지 이벤트
def pause():
    global running, start_time, elapsed_time, prev_elapsed_time
    running = False
    prev_elapsed_time = elapsed_time
# 시간측정 리셋 이벤트
def reset():    
    global running, start_time, elapsed_time, prev_elapsed_time
    running = False
    elapsed_time = 0.0
    prev_elapsed_time = 0.0
    timeText.configure(text=str(elapsed_time))


# 윈도우 초기 설정
window = Tk()
timer = 0
start_time = time.time()
stop_time = time.time()
elapsed_time = 0.0
prev_elapsed_time = 0.0

# 화면 출력 설정
window.title("Simple StopWatch")
timeText = Label(window, height = 5, text="0", font=("Arial 40 bold"))
timeText.pack(side = TOP)
startButton = Button(window, width=10, text="Start", bg="green", command=start)
startButton.pack(side = LEFT)
stopButton = Button(window, width=10, text="Pause", bg="red", command=pause)
stopButton.pack(side = LEFT)
resetButton = Button(window, width=10, text="Reset", bg="yellow", command=reset)
resetButton.pack(side = LEFT)

if __name__ == '__main__':
    runTimer()
    window.mainloop()

