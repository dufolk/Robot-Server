from ..utils import *
import socketserver
# Author : ryk
# 用于发布比赛命令的服务

class CommandPublishService():
    def publish(command:str):
        msg = myencoder(command)
        GlobalStatus.SendLock.acquire()
        try:
            for client in GlobalStatus.Clients:
                client.entity.sendall(msg)
        finally:
            GlobalStatus.SendLock.release()
