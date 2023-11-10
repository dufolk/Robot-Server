# 
import threading
import time
import sys
sys.path.append('.')
from .client_model import ClientModel
from configs import *
from src.models import Location
from src.utils import *

class RobotEntity(ClientModel):
    def __init__(self, server_ip, server_port, id:int):
        super().__init__(server_ip, server_port)
        self.id = id
        self.robot_connect()
        self.global_location = dict()
        self.location = Location()
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
                print(msg)
                self.task(json.loads(msg))  
            except Exception as e:
                print(e)
                continue

    def robot_connect(self):
        self.connect()
        self.send_message(str(self.id))

# 根据报文类型进行不同的处理
    def task(self, msg:dict):
        type = msg_type(msg)
        if type == Config.MSG_TYPE['LOCATION']:
            self.global_location = msg
        # TODO: 用于根据报文类型进行不同的处理
        else:
            pass

# 向其他机器人发送消息
    def send2message(self, to:int, msg:str):
        msg2robo = {
            "from": str(self.id),
            "to": str(to),
            "msg": msg
        }

        self.sock.send(myencoder(json.dumps(msg2robo)))
        print("Send Message Successfully!")

        



# {"id":[x,y,z], ...}
# {"from":"id", "msg":"value"}
# {"from":"id", "to":"id", "msg":"value"}
            
            

    