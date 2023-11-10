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

    def recv_msg(self):
        self.type = 1
        while True:
            try:
                self.type = 1
                msg_len = self.sock.recv(4).decode('utf-8')
                msg_len = int(msg_len)
                self.msg = mydecoder(self.sock.recv(msg_len))
                if self.msg == None:
                    continue
                self.task()  
            except Exception as e:
                print(e)
                continue

    def robot_connect(self):
        self.connect()
        self.send_message(2, "Hello robot!")

    def task(self):
        type = msg_type(self.msg)
        if type == Config.MSG_TYPE['LOCATION']:
            self.global_location = json.loads(self.msg)
            print(self.location.location)
        # TODO: 用于根据报文类型进行不同的处理
        else:
            pass

# 向服务器发送消息
    def send_message(self, to:int, msg):
        msg2robo = {
            "from": self.id,
            "to": str(to),
            "msg": msg
        }
        msg2robo = json.dumps(msg2robo)
        msg2robo = myencoder(msg2robo)
        self.sock.send(msg2robo)
        print("Send Message Successfully!")

        



# {"id":[x,y,z], ...}
# {"from":"id", "msg":"value"}
# {"from":"id", "to":"id", "msg":"value"}
            
            

    