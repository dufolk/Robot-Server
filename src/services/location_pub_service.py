from ..utils import *
import threading
import time
# Author ： ZP
# 用于发布坐标的服务
class LocationPubService:
    def __init__(self):
        t = threading.Thread(target=self.publish)
        t.setDaemon(True) # 设置为守护线程, 主线程结束时, 该线程也结束
        t.start()

    def publish(self):
        while True:
            location_message = format_location()
            for client in GlobalStatus.Clients:
                client.entity.sendall(location_message.encode('utf-8'))
            time.sleep(0.05)

