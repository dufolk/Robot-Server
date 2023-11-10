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
        client.send2message(2, 'Hello')
        time.sleep()

    # print("Finished!")
