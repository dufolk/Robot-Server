import threading

# Author ： ZP
# 用于存储全局状态
class GlobalStatus:
    # 用于存储所有已连接的客户端
    Clients = dict()

    # 全局发送数据的线程锁
    SendLock = threading.Lock()

    SpeechFlag = False