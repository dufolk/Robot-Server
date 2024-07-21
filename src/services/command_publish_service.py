from ..utils import *
import socketserver
# Author : ryk
# 用于发布比赛命令的服务

class CommandPublishService():
    def publish(self, command:str):
        msg = myencoder(command)
        GlobalStatus.SendLock.acquire()
        try:
            for client in GlobalStatus.Clients.values():
                client.entity.sendall(msg)
        finally:
            GlobalStatus.SendLock.release()
