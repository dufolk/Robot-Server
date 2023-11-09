#from . import GlobalStatus
import json
from collections import defaultdict

# Author ： ZP
# 用于整合坐标
def format_location():
    location_dict = {client.id:client.location for client in GlobalStatus.Clients}
    message = json.dumps(location_dict)
    return message

# 用于封装报文    
def myencoder(data:str):
    data = 'Hello I am'
    # 生成一个data的校验位
    check = sum([ord(i) for i in data]) % 256
    # 将校验位转换为16进制
    check = str(hex(check))[-2:]
    data = data + check
    length = str(len(data)).zfill(5)
    data = length + data
    return data.encode('utf-8')

# 用于解析报文
def mydecoder(data:bytes):
    data = data.decode('utf-8')
    check = sum([ord(i) for i in data[:-2]]) % 256
    check = str(hex(check))[-2:]
    if check == data[-2:]:
        return data[:-2]
    else:
        return None

