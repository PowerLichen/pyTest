import socket

Port_Num = 18080
hostname = socket.gethostname()
hostAddr = socket.gethostbyname(hostname)

clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSock.connect((hostAddr, Port_Num))