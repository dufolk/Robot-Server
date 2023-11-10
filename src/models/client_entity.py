from . import Location

# Author ： ZP
# 服务器记录的客户端实体
class ClientEntity(Location):
    def __init__(self, id:int, entity):
        super().__init__()
        self.id = id
        self.entity = entity

    def __str__(self):
        return f"Location: {self.location}"

