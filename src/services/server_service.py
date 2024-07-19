import socketserver
import json
from ..utils import *
from . import TaskManager
from ..models import ClientEntity
from configs import Config

# Author ： ZP
# 用于处理客户端的请求
class ServerService(socketserver.BaseRequestHandler):                              
    def handle(self):
        print('Got connection from', self.client_address)
        self.id = int(self.myrecv())
        currclient = ClientEntity(self.id, self.request)
        self.disconnect = False
        GlobalStatus.Clients[self.id] = currclient

        while True:
            data = self.myrecv()
            if self.disconnect:
                break
            if data == None:
                continue
            else:
                TaskManager.task_manage(json.loads(data))

        print('Lost connection from', self.client_address)
        GlobalStatus.Clients.pop(self.id)

    def myrecv(self) -> str:
        try:
            bufferdata = self.request.recv(4)
            if not bufferdata:
                self.disconnect = True
                return None
            length = int(bufferdata.decode('utf-8'))
        except OSError:
            self.disconnect = True
            return None
        except Exception as e:
            print('myrecv error:', e)
            return None
        data = self.request.recv(length)
        data = mydecoder(data)
        return data
    
if __name__ == '__main__':
    host = Config.SERVER_IP
    port = Config.SERVER_PORT
    server = socketserver.ThreadingTCPServer((host, port), ServerService)
    print('server started')
    server.serve_forever()

        

        
