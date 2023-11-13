from configs import Config
from ..utils import *

# Author ： ZP
class TaskManager:
    # 根据报文类型进行不同的处理
    def task_manage(msg:dict):
        type = msg_type(msg)
        # print(msg)
        if type == Config.MSG_TYPE['SERVER_COMMAND']:
            client_send_msg(**msg)
        elif type == Config.MSG_TYPE['LOCATION']:
            GlobalStatus.Clients[msg['id']].location = msg['location']