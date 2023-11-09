from .locations import Location
# Author ： ZP
# 服务器记录的客户端实体
class ClientEntity:
    def __init__(self, id:int, entity):
        self.id = id
        self.location = Location()
        self.entity = entity

