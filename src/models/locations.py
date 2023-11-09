# Author ： ZP
# 坐标类
class Location:
    def  __init__(self):
        self.__x = 0
        self.__y = 0
        self.__yaw = 0

    @property
    def location(self):
        return (self.__x, self.__y, self.__yaw)
    
    @location.setter
    def location(self, location):
        self.__x = location[0]
        self.__y = location[1]
        self.__yaw = location[2]

    def __str__(self):
        return f"Location: {self.location}"
