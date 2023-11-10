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
        self.disconnect = False
        GlobalStatus.Clients[self.id] = currclient

        while True:
            print('Waiting for data from', self.client_address)
            data = self.myrecv()
            print('Received', data, 'from', self.client_address)
            if self.disconnect:
                break
            if data == None:
                continue
            else:
                self.task(json.loads(data))

        print('Lost connection from', self.client_address)
        GlobalStatus.Clients.pop(self.id)

    def command_publish(self, command:str):
        CommandPublishService.publish(command)

    def myrecv(self) -> str:
        try:
            bufferdata = self.request.recv(4)
            if not bufferdata:
                self.disconnect = True
                return None
            length = int(bufferdata.decode('utf-8'))
        except Exception as e:
            print('myrecv error:', e)
            return None
        data = self.request.recv(length)
        data = mydecoder(data)
        return data
    
    def send_msg(self, **command):
        data = {
            "from": command['from'],
            "msg": command['msg']
        }
        GlobalStatus.SendLock.acquire()
        if command['to'] in GlobalStatus.Clients.keys():
            GlobalStatus.Clients[command['to']].entity.sendall(myencoder(json.dumps(data)))
        GlobalStatus.SendLock.release()

    # 根据报文类型进行不同的处理
    def task(self, msg:dict):
        type = msg_type(msg)
        # print(msg)
        if type == Config.MSG_TYPE['SERVER_COMMAND']:
            self.send_msg(**msg)
        elif type == Config.MSG_TYPE['LOCATION']:
            GlobalStatus.Clients[str(msg['id'])].location = msg['location']
            # print([client.location for client in GlobalStatus.Clients.values()])

        
