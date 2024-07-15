from src.services import ServerService, LocationPubService
from src.services import CommandPublishService
from src.utils import GlobalStatus
from src.views import WebService
from configs import Config

import socketserver
from flask import Flask, render_template

if __name__ == '__main__':
    host = Config.SERVER_IP
    port = Config.SERVER_PORT
    server = socketserver.ThreadingTCPServer((host, port), ServerService)
    app = WebService()
    location_pub = LocationPubService()
    print('server started')
    server.serve_forever()
    

