from flask import render_template
from flask import Blueprint
from flask_socketio import SocketIO
from ..services import SpeechService, CommandPublishService
import random
from ..utils import *
import time

import threading

views_blue = Blueprint('views', __name__)
socketio = SocketIO()
ss = SpeechService()
cs = CommandPublishService()
# 测试血量/速度/热值
redblood=[[1.2,0,2000],[1.2,0,1940],[1.2,0,1880],[1.2,0,1820],[1.2,10,1760],[0,20,1760],[0,15,1760],[1.2,15,1760],[1.2,10,1760],[1.2,10,1760],[1.2,15,1700]]
blueblood=[[1.0,30,2000],[0,40,2000],[0.7,50,1940],[1.0,50,1820],[0,40,1760],[0.5,35,1700],[0.5,35,1700],[0.2,40,1700],[0.2,45,940],[0,50,580],[0.4,55,520]]
a=[0,0,2000]     
b=[0,0,2000]  
               
# Author : ZP
# 用于启动服务
@views_blue.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def connect(message):
    print('WEB connect')
    socketio.start_background_task(send_location)
    socketio.start_background_task(blood_test)
   
    
def send_location():
    while True:
        loc = {k:[v.location[0],v.location[1]] for k,v in GlobalStatus.Clients.items()}
        data = loc
        socketio.emit('message', data)
        time.sleep(0.1)

# 测试robot传送数据
def blood_test():
    i=0
    while True:
        a=redblood[i]
        b=blueblood[i]
        data_test=a
        blue_test=b
        socketio.emit('message_test', data_test)
        socketio.emit('msg_blue', blue_test)
        time.sleep(1)

@socketio.on('b1SS')
def speech_service():
    mode = ss.record_and_recog()
    msg = {"from":"server", "msg":str(mode)}
    msg = json.dumps(msg)
    cs.publish(msg)
    
