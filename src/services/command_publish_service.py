from ..utils import GlobalStatus
# Author : ryk
# 用于发布比赛命令的服务

class CommandPublishService():
    def publish(self,command):
        for client in Clients:
            self.sendall(command)
