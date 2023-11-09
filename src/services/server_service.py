import socketserver
import json
from ..utils import GlobalStatus
from . import CommandPublishService
import time 

# Author ： ZP
# 用于处理客户端的请求
class ServerService(socketserver.BaseRequestHandler):                              
    def handle(self):
        print('Got connection from', self.client_address)
        GlobalStatus.Clients.append(self.request)
        while self.request.recv(1):
            self.command_publish("Hello")
            time.sleep(1)

    def command_publish(self, command):
        CommandPublishService.publish(command)

        
