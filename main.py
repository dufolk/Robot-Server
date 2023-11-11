from src.services import ServerService
from src.services import LocationPubService
from src.services import CommandPublishService
from configs import Config
import socketserver

if __name__ == '__main__':
    host = Config.SERVER_IP
    port = Config.SERVER_PORT
    server = socketserver.ThreadingTCPServer((host, port), ServerService)
    location_pub = LocationPubService()
    print('server started')
    server.serve_forever()

    