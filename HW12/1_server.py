"""
  Project: Homework 12.1
  Author: 최민수
  StudentID: 21511796
  Date of last update: May. 31, 2021
  Detail: 파이썬 스레드 기반의 채팅 프로그램. 서버 사이드를 구현
"""

import socket, sys, threading
from threading import Thread
from time import sleep
import tkinter as tk
from tkinter import ttk, scrolledtext, END

SocketChat_PortNumber = 24000

class SocketChatting:
    # 초기 설정
    def __init__(self, mode):
        global hostAddr
        self.win = tk.Tk()
        self.mode = mode
        
        self.win.title("Multi-thread-based SOcket Chatting(TCP Server)")
        hostname = socket.gethostname()
        hostAddr = socket.gethostbyname(hostname)
        print("My (server) IP address = {}".format(hostAddr))
        self.myAddr = hostAddr
        self.createWidgets()

        serv_thread = Thread(target=self.TCPServer, daemon=True)
        serv_thread.start()

    # TCP 서버 연결
    def TCPServer(self):
        self.servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servSock.bind((hostAddr, SocketChat_PortNumber))
        self.scr_servDisplay.insert(tk.INSERT,"TCP server is waiting for a client .... \n" )
        self.servSock.listen(1)
        self.conn, self.cliAddr = self.servSock.accept()
        print("TCP Server is connected to client ({})\n".format(self.cliAddr))
        self.scr_servDisplay.insert(tk.INSERT, "TCP server is connected to client\n")
        self.scr_servDisplay.insert(tk.INSERT, "TCP client IP address : {}\n".format(self.cliAddr[0]))
        self.peerAddr_entry.insert(END, self.cliAddr[0])
        while True:
            servRecvMsg = self.conn.recv(512).decode()
            if not servRecvMsg:
                break
            self.scr_servDisplay.insert(tk.INSERT, ">>" + servRecvMsg)
        self.conn.close()
    
    #종료
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    #메시지 전송
    def serv_send(self):
        msgToCli = str(self.scr_servInput.get(1.0, END))
        self.scr_servDisplay.insert(tk.INSERT, "<<" + msgToCli)
        self.conn.send(bytes(msgToCli.encode()))
        self.scr_servInput.delete('1.0', END)
    
    #GUI 구성
    def createWidgets(self):
        frame = ttk.LabelFrame(self.win, text="Frame(Socket-based Text Message Chatting)")
        frame.grid(column=0, row=0, padx=8, pady=4)

        frame_addr_connect = ttk.LabelFrame(frame, text="")
        frame_addr_connect.grid(column=0, row=0,padx=40, pady=20, columnspan=2)

        myAddr_label = ttk.Label(frame_addr_connect, text="MyAddr(Server)")
        myAddr_label.grid(column=0, row=0, sticky='W') #
        peerAddr_label = ttk.Label(frame_addr_connect, text="Peer(CLient)Addr")
        peerAddr_label.grid(column=1, row=0, sticky='W')

        self.myAddr = tk.StringVar()
        self.myAddr_entry = ttk.Entry(frame_addr_connect, width=15, textvariable=self.myAddr)
        self.myAddr_entry.insert(END, hostAddr)
        self.myAddr_entry.grid(column=0, row=1, sticky='W')

        self.peerAddr = tk.StringVar()
        self.peerAddr_entry = ttk.Entry(frame_addr_connect, width=15, textvariable="")
        self.peerAddr_entry.grid(column=1, row=1, sticky='W')

        scrol_w, scrol_h = 40, 20
        servDisplay_label = ttk.Label(frame, text="Socket Server Display")
        servDisplay_label.grid(column=0, row=1 )
        self.scr_servDisplay = scrolledtext.ScrolledText(frame, width=scrol_w, height=scrol_h, wrap=tk.WORD)
        self.scr_servDisplay.grid(column=0, row=2, sticky='E')

        servInput_label = ttk.Label(frame, text="Input Text Message (Server) :")
        servInput_label.grid(column=0, row=3 )

        self.scr_servInput = scrolledtext.ScrolledText(frame, width=40, height=3, wrap=tk.WORD)
        self.scr_servInput.grid(column=0, row=4)

        serv_send_button = ttk.Button(frame, text="Send Message to Client", command=self.serv_send)
        serv_send_button.grid(column=0, row=5, sticky='E')

        self.scr_servInput.focus()


print("Running TCP server")
sockChat = SocketChatting("server")
sockChat.win.mainloop()
