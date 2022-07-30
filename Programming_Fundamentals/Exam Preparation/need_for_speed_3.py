def buy_cars():
    n = int(input())
    for _ in range(n):
        car, mileage, fuel = input().split('|')
        garage[car] = {'mileage': int(mileage), 'fuel': int(fuel)}


def use_cars():
    while True:
        command = input().split(' : ')
        action = command[0]

        if action == 'Stop':
            break

        car = command[1]

        if action == 'Drive':
            distance = int(command[2])
            fuel = int(command[3])

            if garage[car]['fuel'] < fuel:
                print("Not enough fuel to make that ride")
            else:
                garage[car]['mileage'] += distance
                garage[car]['fuel'] -= fuel
                print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

            if garage[car]['mileage'] >= 100_000:
                garage.pop(car)
                print(f"Time to sell the {car}!")

        elif action == 'Refuel':
            fuel = int(command[2])
            current_fuel = garage[car]['fuel']
            if current_fuel + fuel > 75:
                garage[car]['fuel'] = 75
                print(f'{car} refueled with {75-current_fuel} liters')
            else:
                garage[car]['fuel'] += fuel
                print(f'{car} refueled with {fuel} liters')

        elif action == 'Revert':
            km = int(command[-1])
            garage[car]['mileage'] -= km
            if garage[car]['mileage'] < 10_000:
                garage[car]['mileage'] = 10_000
                continue
            print(f"{car} mileage decreased by {km} kilometers")


def whats_in_garage():
    for car in garage:
        print(f"{car} -> Mileage: {garage[car]['mileage']} kms, Fuel in the tank: {garage[car]['fuel']} lt.")


garage = {}
buy_cars()
use_cars()
whats_in_garage()