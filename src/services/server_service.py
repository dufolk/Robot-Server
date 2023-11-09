import socketserver
import json
from ..utils import GlobalStatus
from . import CommandPublishService

# Author ： ZP
# 用于处理客户端的请求
class ServerService(socketserver.BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        clienteneity = 1
        GlobalStatus.Clients.append(self.request)
        print(GlobalStatus.Clients)

class RobotServer:
    def commandpublish(self, command):
        CommandPublishService.publish(command)

        
