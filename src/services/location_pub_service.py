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
                clients = GlobalStatus.Clients.values()
                for client in clients:
                    client.entity.sendall(msg)
            except Exception as e:
                print(e)
            finally:
                GlobalStatus.SendLock.release()
            
            time.sleep(0.05)

