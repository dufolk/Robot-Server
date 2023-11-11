class Config:
    # 主机等待客户端发送消息时间
    WAIT_TIMEOUT = 5

    # 报文类型
    MSG_TYPE = {
        "LOCATION": 0,
        "MESSAGE": 1,
        "SERVER_COMMAND": 2,
    }

    # 服务器IP和端口
    SERVER_IP = "192.168.0.5"
    SERVER_PORT = 19999