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

    color_id = {"RED1":0, "RED2":1, "BLUE1":2, "BLUE2":3}