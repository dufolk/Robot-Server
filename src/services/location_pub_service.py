from ..utils import *
import threading
import time

import random
# Author ： ZP
# 用于发布坐标的服务
class LocationPubService:
    def __init__(self):
        t = threading.Thread(target=self.publish)
        t.setDaemon(True) # 设置为守护线程, 主线程结束时, 该线程也结束
        t.start()

    def publish(self):
        # while True:
        #     from ..views import socketio
        #     if type(socketio) == None:
        #         continue
        #     print("初始化成功")
        #     sockio = socketio
        #     break
        while True:
            location_message = format_location()
            # self.web_view(sockio)
            if location_message == None:
                continue
            msg = myencoder(location_message)
            GlobalStatus.SendLock.acquire()
            try:
                for client in GlobalStatus.Clients.values():
                    client.entity.sendall(msg)
            finally:
                GlobalStatus.SendLock.release()
            
            time.sleep(0.05)

    def web_view(self, socketio):
        # if len(GlobalStatus.Clients) == 0:
        #     return None
        # location_dict = {id:client.location[:-1] for id, client in GlobalStatus.Clients.items()}
        # location_dict = [client.location[:-1] for id, client in GlobalStatus.Clients.items()]
        loc = [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
        print(loc)
        data = {'msg': loc}
        socketio.emit('message', data)
        time.sleep(0.05)
