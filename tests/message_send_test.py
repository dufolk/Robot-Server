from models import RobotEntity
import sys
import time
import socket
sys.path.append('.')
from src.utils import *
from configs import *
import json
if __name__ == '__main__':
<<<<<<< HEAD
    client = RobotEntity(Config.SERVER_IP, Config.SERVER_PORT, 1)
    while True:
        msg = client.location
        # msg = json.dumps(msg)
        # client.send_message(msg)
        time.sleep(0.05)
=======
    try:
        client = RobotEntity(Config.SERVER_IP, Config.SERVER_PORT, id="BLUE2")
        while True:
            msg = client.location
            # client.send2message(2, 'Hello')
            time.sleep(1)
    except KeyboardInterrupt:
        client.sock.shutdown(socket.SHUT_RDWR)
        client.sock.close()
        
>>>>>>> develop

    # print("Finished!")
