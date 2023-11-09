class Location:
    def  __init__(self, id, location):
        self.__id = id
        self.__location = location
        
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,value):
        self.__id=value

    @property
    def location(self):
        return self.__location

    def __str__(self):
        return self.__id
