import threading
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_cors import CORS
from . import views_blue, socketio

# Author : ZP
# 前端连接服务
class WebService:
    def __init__(self):
        self.web_service_thread = threading.Thread(target=self.web_service)
        self.web_service_thread.setDaemon(True)
        self.web_service_thread.start()

    def web_service(self):
        app = Flask(__name__)
        CORS(app)
        app.register_blueprint(views_blue)
        socketio.init_app(app, cors_allowed_origins="*")
        # app.run(host="0.0.0.0", port=8000)
        socketio.run(app, host="0.0.0.0", port=8000)
        # socketio.run(app, host="192.168.1.10", port=8000)