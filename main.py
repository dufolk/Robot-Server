from src.services import ServerService
from src.services import LocationPubService
import socketserver

if __name__ == '__main__':

    host = '192.168.1.8'
    port = 9999
    server = socketserver.ThreadingTCPServer((host, port), ServerService)
    print('server started')
    server.serve_forever()

    