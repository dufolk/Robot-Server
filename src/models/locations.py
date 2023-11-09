class Location:
    def  __init__(self):
        self.__location = [0] * 3

    @property
    def location(self):
        return self.__location
    
    @location.setter
    def location(self, location):
        self.__location = location

    def __str__(self):
        return f"Location: {self.__location}"

