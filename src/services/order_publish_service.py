class OrderPublishService:
    def publish():
        for client in clients:
            client.sendall("start")