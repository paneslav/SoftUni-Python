from collections import deque

fuel_pumps_amount = int(input())

current_fuel = 0
pump_counter = 0
fuel_pumps = deque()

for i in range(fuel_pumps_amount):
    amount_of_petrol, distance_to_next_pump = input().split()
    fuel_pumps.append((int(amount_of_petrol), int(distance_to_next_pump), i))

# print(fuel_pumps)

while True:

    if pump_counter == fuel_pumps_amount - 1:
        print(fuel_pumps[0][-1])
        break

    amount_of_petrol = fuel_pumps[pump_counter][0]
    distance_to_next_pump = fuel_pumps[pump_counter][1]
    pump_index = fuel_pumps[pump_counter][-1]

    current_fuel += amount_of_petrol

    if current_fuel < distance_to_next_pump:
        fuel_pumps.append(fuel_pumps.popleft())
        current_fuel = 0
        pump_counter = 0
    else:
        current_fuel -= distance_to_next_pump
        pump_counter += 1


