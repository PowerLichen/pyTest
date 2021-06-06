"""
  Project: Homework 13.3
  Author: 최민수
  StudentID: 21511796
  Date of last update: June. 7, 2021
  Detail:  Web 서버 기반 원격 게임 기능 구현
"""

import turtle
import threading
import socket
from queue import Queue
from _thread import *
from bottle import route, run, get, post, response, static_file, request
from Remote_controlled_drawing import *
Port_Num = 18080
hostname = socket.gethostname()
hostAddr = socket.gethostbyname(hostname)
servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servSock.bind((hostAddr, Port_Num))
print("Web server ({}) is waiting a client to connect ....".format(hostAddr))
servSock.listen(1)
sock_conn, cliAddr = servSock.accept()
print("Web Server is connected to the RC_Drawing client ({})...".format(cliAddr))

@route('/') # invoked
def do_root_index():
    print("do_root_index('/') is invoked ==> ./index.html will be executed ...")
    return static_file("index.html", root=".")

@route('/demo') # invoked by localhost:8080/demo
def do_demo():
    print("do_demo('/demo') was invoked ...")
    return "<H2>do_demo('/demo') was invoked ...</H2>"

@route('/login', method='GET')
def login():
    return '''
        <form action="/login" method="post">
        Username: <input name="username" type="text"/>
        Password: <input name="password" type="password" />
        <input value="Login" type="submit" />
        </form>
    '''
@route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    passwd = request.forms.get('password')
    return "login (user_name = {}, passwd = {})".format(username, passwd)

@route('/remote_control', method='POST')
def rc_POST():
    recv_cmd=request.forms.get('command')
    print("rc_POST({}) was invoked ...".format(recv_cmd))
    return_msg = "result of {}".format(recv_cmd)
    print("return_msg = {}".format(return_msg))
    return return_msg

@route('/remote_control', method='GET')
def rc_GET():
    print("rc_GET() was invoked ...")
    return_value = '7'
    return_msg = "result of RC_GET = {}".format(return_value)
    print("return_msg = {}".format(return_msg))
    return return_msg

@route('/remote_control', method='PUT')
def rc_PUT():
    recv_cmd=request.forms.get('put_value')
    print("rc_PUT({}) was invoked ...".format(recv_cmd))
    return_msg = "result of {}".format(recv_cmd)
    print("return_msg = {}".format(return_msg))
    return return_msg

@route('/remote_drawing_shape', method='POST')
def remote_drawing_shape_POST():
    shape_name = request.forms.get('remote_drawing_shape')
    print("Web Server::remote_drawing shape({}) was invoked ...".format(shape_name))
    msg_to_rc_drawing = "change_shape " + shape_name
    sock_conn.send(bytes(msg_to_rc_drawing.encode()))
    return_msg = "Web server::remote_drawn_shape({})".format(shape_name)
    print("return_msg = {}".format(return_msg))
    return return_msg

@route('/remote_drawing_color', method='POST')
def rgb_color_set_POST():
    rgb_value=request.forms.get('rgb_value')
    print("/remote_drawing ‐ rgb_color_set_POST({}) was invoked ...".format(rgb_value))
    msg_to_rc_drawing = "change_color " + rgb_value
    sock_conn.send(bytes(msg_to_rc_drawing.encode()))
    return_msg = "Web server::rgb_color_set ({})".format(rgb_value)
    print("return_msg = {}".format(return_msg))
    return return_msg
#‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐
run(host='', port=8080, server='paste')