from flask import render_template
from flask import Blueprint
from flask_socketio import SocketIO
import random
from ..utils import *
import time

views_blue = Blueprint('views', __name__)
socketio = SocketIO()

# Author : ZP
# 用于启动服务
@views_blue.route('/')
def index():
    return render_template('index.html')

# @socketio.on('message')
# def message(msg):
#     print(msg)
#     loc = [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
#     data = {'msg': loc}
#     socketio.emit('message', data)

@socketio.on('connect')
def connect(message):
    print('connect')
    socketio.start_background_task(send_location)
    
def send_location():
    while True:
        loc = {k:[v.location[0],v.location[1]] for k,v in GlobalStatus.Clients.items()}
        data = loc
        socketio.emit('message', data)
        time.sleep(0.1)