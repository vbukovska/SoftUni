class Town:
    def __init__(self, name):
        self.name = name
        self.latitude = ''
        self.longitude = ''

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def __repr__(self):
        representation = [f'Town: {self.name}', f'Latitude: {self.latitude}', f'Longitude: {self.longitude}']
        return ' | '.join(representation)


town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)
