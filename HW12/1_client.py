import socket, sys, threading
from threading import Thread # for testing multi-thread
from time import sleep #for sleep in thread
import tkinter as tk
from tkinter import ttk, scrolledtext, END

LocalHost = "127.0.0.1"
SocketChat_PortNumber = 24000

class SocketChatting:
    def __init__(self, mode):
        global hostAddr
        self.win = tk.Tk()
        self.mode = mode
        
        self.win.title("Multi-thread-based SOcket Chatting(TCP Client)")
        hostname = socket.gethostname()
        hostAddr = socket.gethostbyname(hostname)
        print("My (client) IP address = {}".format(hostAddr))
        self.myAddr = hostAddr
        self.createWidgets()

        cli_thread = Thread(target=self.TCPClient, daemon=True)
        cli_thread.start()

    def TCPServer(self):
        self.cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servAddr_str = input("Server IP Addr(e.g., '127.0.0.1)=")
        self.cliSock.connect((servAddr_str, SocketChat_PortNumber))
        servAddr = self.cliSock.getpeername()
        print("TCP Client is connected to server ({})\n".format(servAddr))
        self.scr_cliDisplay.insert(tk.INSERT,"TCP client is connected to server \n")
        self.scr_cliDisplay.insert(tk.INSERT,"TCP server IP address : {}\n".format(servAddr[0]) )
        self.servAddr_entry.insert(END, servAddr[0])
        while True:
            cliRecvMsg = self.cliSock.recv(8192).decode()
            if not cliRecvMsg:
                break
            self.scr_cliDisplay.insert(tk.INSERT,">> " + cliRecvMsg)
        self.cliSock.close()

    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    def connect_server(self):
        self.scr_cliDisplay.insert(tk.INSERT,"Connecting to server ....")
        self.myIpAddr = self.myAddr.get()
        self.peerIpAddr = self.peerAddr.get()
        self.scr_cliDisplay.insert(tk.INSERT, "My IP Address : " + self.myIpAddr + '\n')
        self.scr_cliDisplay.insert(tk.INSERT, "Server's IP Address : " + self.peerIpAddr + '\n')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.peerIpAddr, SocketChat_PortNumber))

    
    def cli_send(self): # to peer/server
        msgToServer = str(self.scr_cliInput.get(1.0, END))
        self.scr_cliDisplay.insert(tk.INSERT,"<< " + msgToServer)
        self.cliSock.send(bytes(msgToServer.encode()))
        self.scr_cliInput.delete('1.0', END)

    def createWidgets(self):
        frame = ttk.LabelFrame(self.win, text="Frame (Socket-based Text Message Chatting)")
        frame.grid(column=0, row=0, padx=8, pady=4)

        frame_addr_connect = ttk.LabelFrame(frame, text="")
        frame_addr_connect.grid(column=0, row=0, padx=40, pady=20, columnspan=2)

        myAddr_label = ttk.Label(frame_addr_connect, text="MyAddr (Client)")
        myAddr_label.grid(column=0, row=0, sticky='W')
        peerAddr_label = ttk.Label(frame_addr_connect, text="Server Addr")
        peerAddr_label.grid(column=1, row=0, sticky='W')

        self.myAddr = tk.StringVar()
        self.myAddr_entry = ttk.Entry(frame_addr_connect, width=15, textvariable=self.myAddr)
        self.myAddr_entry.insert(END, hostAddr)
        self.myAddr_entry.grid(column=0, row=1, sticky='W')

        self.servAddr = tk.StringVar()
        self.servAddr_entry = ttk.Entry(frame_addr_connect, width=15, textvariable="")
        self.servAddr_entry.grid(column=1, row=1, sticky='W')

        connect_button = ttk.Button(frame_addr_connect, text="Connect", command=self.connect_server)
        connect_button.grid(column=3, row=1)
        connect_button.configure(state='disabled')

        cliDisplay_label = ttk.Label(frame, text="Socket Client Display")
        cliDisplay_label.grid(column=0, row=1 )
        scrol_w, scrol_h = 40, 20
        self.scr_cliDisplay = scrolledtext.ScrolledText(frame, width=scrol_w,\
        height=scrol_h, wrap=tk.WORD)
        self.scr_cliDisplay.grid(column=0, row=2, sticky='WE') #, columnspan=3
        cliInput_label = ttk.Label(frame, text="Input Text Message (Client) :")
        cliInput_label.grid(column=0, row=3 )
        self.scr_cliInput = scrolledtext.ScrolledText(frame, width=40, height=3, wrap=tk.WORD)
        self.scr_cliInput.grid(column=0, row=4) #, columnspan=3

        cli_send_button = ttk.Button(frame, text="Send Message to Server", command=self.cli_send)
        cli_send_button.grid(column=0, row=5, sticky='E')

        self.scr_cliInput.focus()



print("Running TCP Client")
sockChat = SocketChatting('client')
sockChat.win.mainloop()