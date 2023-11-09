from .locations import Location

class ClientEntity:
    def __init__(self, name):
        self.name = name
        self.location = Location()

