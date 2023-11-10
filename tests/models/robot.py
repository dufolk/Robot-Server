# 
import threading
import time
import sys
sys.path.append('.')
from .client_model import ClientModel
from src.models import Location
from src.utils import *

class RobotEntity(ClientModel):
    def __init__(self, server_ip, server_port):
        super().__init__(server_ip, server_port)
        self.connect()
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
                self.task()
                time.sleep(0.05)
            except Exception as e:
                print(e)
                continue

    def task(self):
        type = msg_type(self.msg)
        if type == 0:
            self.global_location = json.loads(self.msg)
            self.location.location = self.global_location[self.id]
            print(self.location.location)
        



# {"id":[x,y,z], ...}
# {"from":"id", "msg":"value"}
            
            

    