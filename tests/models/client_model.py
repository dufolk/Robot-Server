# Author : YU
# 用于客户端功能类定义
import socket
import sys
sys.path.append('.')
from src.utils import *

class ClientModel:
    def __init__(self, server_ip, server_port):
        self.server_host = server_ip
        self.server_port = server_port
    
    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.server_host, self.server_port))

    def send_message(self, msg:str):
        msg = myencoder(msg)
        self.sock.send(msg)

    def receive_message(self):
        data = self.sock.recv(1024)
        data = data.decode('utf-8')
        print(data)
