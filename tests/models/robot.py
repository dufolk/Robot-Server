import threading
import time
import sys
sys.path.append('.')
from client_model import ClientModel
from src.models import Location
from src.utils import *

class RobotEntity(ClientModel):
    def __init__(self, server_ip, server_port):
        super().__init__(server_ip, server_port)
        self.connect()
        self.location = Location()
        self.receive_thread = threading.Thread(target=self.recv_location)
        self.receive_thread.setDaemon(True)
        self.receive_thread.start()

    def recv_location(self):
        while True:
            try:
                msg_len = self.sock.recv(4).decode('utf-8')
            except:
                continue
            msg_len = int(msg_len)
            msg = mydecoder(self.sock.recv(msg_len))

            time.sleep(0.05)

    