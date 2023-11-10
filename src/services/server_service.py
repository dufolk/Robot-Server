import socketserver
import json
from ..utils import *
from . import CommandPublishService
from ..models import ClientEntity
from configs import Config
import time 
import select

# Author ： ZP
# 用于处理客户端的请求
class ServerService(socketserver.BaseRequestHandler):                              
    def handle(self):
        print('Got connection from', self.client_address)
        self.id = self.myrecv()
        currclient = ClientEntity(self.id, self.request)
        GlobalStatus.Clients[self.id] = currclient
        while True:
            rlist, _, _ = select.select([self.request], [], [], Config.WAIT_TIMEOUT)
            if not rlist:
                self.command_publish('{"from":"server", "msg":"timeout"}')
                #break
            else:
                data = self.myrecv()

        
        print('Lost connection from', self.client_address)
        GlobalStatus.Clients.remove(currclient)

    def command_publish(self, command:str):
        CommandPublishService.publish(command)

    def myrecv(self) -> str:
        try:
            length = int(self.request.recv(4).decode('utf-8'))
        except:
            self.request.recv(1024)
            return None
        data = self.request.recv(length)
        data = mydecoder(data)
        return data
    
    def task(self):
        type = msg_type(self.msg)
        if type == 0:
            self.global_location = json.loads(self.msg)
            self.location.location = self.global_location[self.id]
            print(self.location.location)
        elif type == 1:
            self.command_publish(self.msg)
        elif type == 2:
            self.id = self.msg
            self.request.sendall(myencoder('{"from":"server", "msg":"ok"}'))
        elif type == 3:
            self.request.sendall(myencoder(format_location()))
        else:
            pass

        
