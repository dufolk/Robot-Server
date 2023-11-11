import threading
from flask import Flask, render_template
from views import views_blue

class WebService:
    def __init__(self):
        self.web_service = threading.Thread(target=self.web_service)
        self.web_service.setDaemon(True)
        self.web_service.start()

    def web_service(self):
        app = Flask(__name__.split('.')[0])
        print(__name__)
        app.register_blueprint(views_blue)
        app.run(host="0.0.0.0", port=8000)