class Parking:
    def __init__(self):
        self.parking_register = {}

    def registered(self, user):
        is_registered = False
        if user in self.parking_register:
            is_registered = True
        return is_registered

    def register(self, data):
        username = data[0]
        license_plate_number = data[1]
        if self.registered(username):
            result = f'ERROR: already registered with plate number {self.parking_register[username]}'
        else:
            self.parking_register[username] = license_plate_number
            result = f'{username} registered {license_plate_number} successfully'
        return result

    def unregister(self, data):
        username = data[0]
        if not self.registered(username):
            result = f'ERROR: user {username} not found'
        else:
            result = f'{username} unregistered successfully'
            self.parking_register.pop(username)
        return result

    def parking_validation(self, command, data):
        if command == 'register':
            return self.register(data)
        else:
            return self.unregister(data)


number_of_vehicles = int(input())
parking = Parking()

for new_vehicle in range(number_of_vehicles):
    command, *vehicle_data = input().split()
    print(parking.parking_validation(command, vehicle_data))
[print(f"{user} => {plate_number}") for user, plate_number in parking.parking_register.items()]