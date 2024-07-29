from flask import render_template
from flask import Blueprint, Response, stream_with_context
import subprocess
from flask_socketio import SocketIO
from ..services import SpeechService, CommandPublishService
import random
from ..utils import *
import time
import subprocess

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
    print("Rendering index.html")
    return render_template('index.html')

def generate():
    command = [
        'ffmpeg',
        '-i', '/dev/video0',  # 输入视频文件或者设备
        '-f', 'webm',  # 选择输出格式为 WebM
        '-codec:v', 'libvpx',  # 使用 VP8 视频编解码器
        '-b:v', '800k',  # 输出视频比特率
        '-r', '30',  # 输出视频帧率
        '-'
    ]
    print("Starting ffmpeg process...")
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=10**8)
    
    def generate_video_stream():
        try:
            while True:
                data = process.stdout.read(1024)
                if not data:
                    print("No more data from ffmpeg.")
                    time.sleep(1)
                    break
                yield data
        except GeneratorExit:
            print("GeneratorExit: Killing ffmpeg process.")
            process.kill()
            raise
        except Exception as e:
            print(f"Exception: {e}")
            process.kill()
            raise
        finally:
            process.kill()
            print("Killing ffmpeg process.")

    return Response(stream_with_context(generate_video_stream()), content_type='video/webm')

@views_blue.route('/stream')
def stream():
    return generate()

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
    
