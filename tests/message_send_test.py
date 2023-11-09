from models import RobotEntity
import sys
import time
sys.path.append('.')
from src.utils import *
import json
if __name__ == '__main__':
    client = RobotEntity('192.168.1.8', 9999)
    while True:
        msg = client.location
        msg = json.dumps(msg)
        client.send_message(msg)
        time.sleep(0.05)

    # print("Finished!")
