"""
  Project: Homework 12.2
  Author: 최민수
  StudentID: 21511796
  Date of last update: May. 31, 2021
  Detail: 영상 채팅의 서버 사이드를 구현
"""

import socket
import cv2
import numpy as np
from queue import Queue
from _thread import *
SERVER_WEBCAM = 0

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

def video_sendto_client(client_socket, queue):
    while True:
        try:
            if not queue.empty():
                stringData = queue.get()
                client_socket.send(str(len(stringData)).ljust(16).encode())
                client_socket.send(stringData)
        except ConnectionResetError as e:
            break
    client_socket.close()

def video_chat_server(queue):
    server_webcam = cv2.VideoCapture(SERVER_WEBCAM)
    while True:
        ret, serv_frame = server_webcam.read()
        if ret == False:
            continue
        encode_param=[int(cv2.IMWRITE_JPEG_QUALITY), 90]
        result, imgencode = cv2.imencode('.jpg', serv_frame, encode_param)
        img_data = np.array(imgencode)
        stringData = img_data.tostring()
        queue.put(stringData)
        cv2.imshow('Server:: Server_Video', serv_frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

def video_recvfrom_client(client_socket):
    while True:
        length = recvall(client_socket, 16)
        stringData = recvall(client_socket, int(length))
        data = np.frombuffer(stringData, dtype='uint8')
        decimg = cv2.imdecode(data, 1)
        cv2.imshow('Server::Received from Client', decimg)
        key = cv2.waitKey(1)
        if key == 27:
            break


if __name__ == "__main__":
    enclosure_queue = Queue()
    serverAddr = '127.0.0.1'
    PORT = 9999
    hostname = socket.gethostname()
    serverAddr = socket.gethostbyname(hostname)
    print("Server IP address = {}".format(serverAddr))

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((serverAddr, PORT))
    server_socket.listen(1)
    print('Server::Video chatting server started')
    start_new_thread(video_chat_server, (enclosure_queue,))
    print('Server::Waitint for client .... ')
    client_socket, addr = server_socket.accept()
    print('Server::connected to ({} : {})'.format(client_socket, addr))
    start_new_thread(video_sendto_client, (client_socket, enclosure_queue,))

    while True:
        length = recvall(client_socket, 16)
        stringData = recvall(client_socket, int(length))
        data = np.frombuffer(stringData, dtype='uint8')
        decimg = cv2.imdecode(data, 1)
        cv2.imshow('Server::Received from Client', decimg)
        key = cv2.waitKey(1)
        if key == 27:
            break
    
    server_socket.close()