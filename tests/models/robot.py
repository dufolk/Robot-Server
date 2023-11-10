# 
import threading
import time
import sys
sys.path.append('.')
from .client_model import ClientModel
from configs import *
from src.models import Location
from src.utils import *

class RobotEntity(ClientModel, Location):
    def __init__(self, server_ip, server_port, id:int):
        ClientModel.__init__(self, server_ip, server_port) 
        Location.__init__(self)
        self.id = id
        self.robot_connect()
        self.global_location = dict()
        self.lock = threading.Lock()
        self.receive_thread = threading.Thread(target=self.recv_msg)
        self.receive_thread.setDaemon(True)
        self.receive_thread.start()
        self.sending_thread = threading.Thread(target=self.send_msg)
        self.sending_thread.setDaemon(True)
        self.sending_thread.start()

    def recv_msg(self):
        while True:
            try:
                msg_len = self.sock.recv(4).decode('utf-8')
                msg_len = int(msg_len)
                msg = mydecoder(self.sock.recv(msg_len))
                if msg == None:
                    continue
                self.task(json.loads(msg))  
            except Exception as e:
                print('recv_msg:'+e)
                continue
    
    def send_msg(self):
        i=0
        while True:
            try:
                # loc_msg = {"id": self.id, "location": self.location}
                loc_msg = {"id": self.id, "location": [i,i,i]}
                loc_msg = myencoder(json.dumps(loc_msg))
                self.lock.acquire()
                try:
                    self.sock.send(loc_msg)
                finally:
                    self.lock.release()
                time.sleep(1)
            except Exception as e:
                print(e)
                continue
            i+=1
        # pass

    def robot_connect(self):
        self.connect()
        self.send_message(str(self.id))

# 根据报文类型进行不同的处理
    def task(self, msg:dict):
        type = msg_type(msg)
        if type == Config.MSG_TYPE['LOCATION']:
            self.global_location = msg
            print(self.global_location)
        # TODO: 用于根据报文类型进行不同的处理
        else:
            # print(msg)
            pass

# 向其他机器人发送消息
    def send2message(self, to:int, msg:str):
        msg2robo = {
            "from": str(self.id),
            "to": str(to),
            "msg": msg
        }

        msg2robo = myencoder(json.dumps(msg2robo))
        self.lock.acquire()
        try:
            self.sock.send(msg2robo)
        finally:
            self.lock.release()

        



# {"id":[x,y,z], ...}
# {"from":"id", "msg":"value"}
# {"from":"id", "to":"id", "msg":"value"}
            
            

    