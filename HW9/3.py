"""
  Project: Homework 9.3
  Author: 최민수
  StudentID: 21511796
  Date of last update: May. 9, 2021
  Detail: Km과 mile의 양방향 변환 계산기를 구현
"""

from tkinter import *

class Converter:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        # km 부분 작성
        self.m_km =  DoubleVar()
        Entry(frame, textvariable= self.m_km).grid(row=0, column=0)
        Label(frame, text = 'Km').grid(row=0, column=1)
        # mile 부분 작성
        self.m_mile =  DoubleVar()
        Entry(frame, textvariable= self.m_mile).grid(row=0, column=2)
        Label(frame, text = 'Mile').grid(row=0, column=3)
        # 버튼 지정
        btn_KmToMile = Button(frame, text='Km -> Mile', command=self.KmToMile)
        btn_KmToMile.grid(row=1, column=0, columnspan=2)
        btn_MileToKm = Button(frame, text='Mile -> Km', command=self.MileToKm)
        btn_MileToKm.grid(row=1, column=2, columnspan=2)

    # Km to Mile 변환 이벤트
    def KmToMile(self):
        num = self.m_km.get()
        self.m_mile.set(num / 1.60934)
    
    # Mile to Km 변환 이벤트
    def MileToKm(self):
        num = self.m_mile.get()
        self.m_km.set(num * 1.60934)

# tkinter 초기설정
window = Tk()
window.wm_title('Km <-> Mile Converter')
app = Converter(window)
window.mainloop()
