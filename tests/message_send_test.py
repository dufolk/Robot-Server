from models import RobotEntity
import sys
import time
sys.path.append('.')
from src.utils import *
from configs import *
import json
if __name__ == '__main__':
    client = RobotEntity(Config.SERVER_IP, Config.SERVER_PORT, 1)
    while True:
        msg = client.location.location
        # msg = json.dumps(msg)
        # client.send_message(msg)
        time.sleep(0.05)

    # print("Finished!")
