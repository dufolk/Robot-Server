from ..utils import GlobalStatus
import socketserver
# Author : ryk
# 用于发布比赛命令的服务

class CommandPublishService():
    def publish(command:str):
        msg = command.encode('utf-8')
        for client in GlobalStatus.Clients:
            client.entity.sendall(msg)
