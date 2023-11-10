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
        id = self.myrecv()
        currclient = ClientEntity(id, self.request)
        GlobalStatus.Clients.append(currclient)
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

    def myrecv(self):
        try:
            length = int(self.request.recv(4).decode('utf-8'))
        except:
            self.request.recv(1024)
            return None
        data = self.request.recv(length)
        data = mydecoder(data)
        return data

        
