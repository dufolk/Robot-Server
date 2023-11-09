import socketserver
import json
from ..utils import GlobalStatus
from .command_publish_service import CommandPublishService

# Author ： ZP
# 用于处理客户端的请求
class ServerService(socketserver.BaseRequestHandler):                              
    def handle(self):
        print('Got connection from', self.client_address)
        GlobalStatus.Clients.append(self.request)
        print(GlobalStatus.Clients)

    def commandpublish(self, command):
        CommandPublishService.publish(command)

        
