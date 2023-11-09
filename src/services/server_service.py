# socket server服务器，用于接受四个机器人的定位消息并发布回去
import socketserver
import time
import json

RED1 = -1
RED2 = -2
BLUE1 = 1
BLUE2 = 2
locations = {RED1: [0,0,0], RED2: [0,0,0], BLUE1: [0,0,0], BLUE2: [0,0,0]}

class ServerService(socketserver.BaseRequestHandler):
    def __init__(self):
        self.clients = []
        super().__init__()

    def handle(self):
        print('Got connection from', self.client_address)
        self.clients.append(self.request)  # Add the client to the list of clients
        while True:
            try:
                data = self.request.recv(1024)
                if not data:
                    print('client disconnected')
                    self.clients.remove(self.request)  # Remove the client from the list of clients
                    break
                data = data.decode('utf-8')
                data = json.loads(data)
                locations[int(data['id'])] = data['location']
                data = json.dumps(locations)
                print(data)
                # 发送给所有客户端·
                for client in self.clients:
                    client.sendall(data.encode('utf-8'))
            except Exception as e:  # Add an except clause to handle exceptions
                print(e)
    

                
if __name__ == '__main__':
    host = 'localhost'
    port = 9999
    server = socketserver.ThreadingTCPServer((host, port), ServerService)
    print('server started')
    server.serve_forever()