from . import GlobalStatus
import json
from collections import defaultdict

# Author ： ZP
# 用于整合坐标
def format_location():
    location_dict = {client.id:client.location for client in GlobalStatus.Clients}
    message = json.dumps(location_dict)
    return message
    
