class Config:
    # 主机等待客户端发送消息时间
    WAIT_TIMEOUT = 5

    # 报文类型
    MSG_TYPE = {
        "LOCATION": 0,
        "MESSAGE": 1,
    }

    # 服务器IP和端口
    SERVER_IP = "192.168.1.8"
    SERVER_PORT = 9999