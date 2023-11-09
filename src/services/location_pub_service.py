from src.models import Location

class LocationPubService:
    def __init__(self):
        self._location = Location()

    def publish(self, location):
        self._location_pub.publish(location)

