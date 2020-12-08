number_of_cars = int(input())

cars_fuel = {}
cars_mileage = {}

for _ in range(number_of_cars):
    car, mileage, fuel = input().split('|')
    mileage = int(mileage)
    fuel = int(fuel)
    cars_fuel[car] = fuel
    cars_mileage[car] = mileage

while True:
    command = input()
    if command == 'Stop':
        break
    command, *car_parameters = command.split(" : ")
    car = car_parameters[0]
    if command == 'Drive':
        mileage = int(car_parameters[1])
        fuel = int(car_parameters[2])
        if cars_fuel[car] < fuel:
            print("Not enough fuel to make that ride")
            continue
        cars_fuel[car] -= fuel
        cars_mileage[car] += mileage
        print(f"{car} driven for {mileage} kilometers. {fuel} liters of fuel consumed.")
        if cars_mileage[car] >= 100000:
            cars_mileage.pop(car)
            cars_fuel.pop(car)
            print(f"Time to sell the {car}!")
    elif command == 'Refuel':
        fuel = int(car_parameters[1])
        if cars_fuel[car] + fuel > 75:
            fuel = 75 - cars_fuel[car]
        cars_fuel[car] += fuel
        print(f"{car} refueled with {fuel} liters")
    else:
        mileage = int(car_parameters[1])
        cars_mileage[car] -= mileage
        if cars_mileage[car] < 10000:
            cars_mileage[car] = 10000
        else:
            print(f"{car} mileage decreased by {mileage} kilometers")

cars_mileage = dict(sorted(cars_mileage.items(), key=lambda x: (-x[1], x[0])))
for car in cars_mileage:
    print(f"{car} -> Mileage: {cars_mileage[car]} kms, Fuel in the tank: {cars_fuel[car]} lt.")

