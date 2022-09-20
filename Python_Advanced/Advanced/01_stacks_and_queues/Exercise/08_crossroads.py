from collections import deque

green_light = int(input())
free_window = int(input())

cars = deque()
total_passed_cars = 0

crash = False

while True:
    car = input()

    if car == 'END':
        break
    elif car == 'green':
        if cars:
            current_car = cars.popleft()
            time_left = green_light - len(current_car)

            while time_left > 0:
                total_passed_cars += 1
                if not cars:
                    break
                current_car = cars.popleft()
                time_left -= len(current_car)

            if time_left == 0:
                total_passed_cars += 1

            if free_window >= abs(time_left):
                if time_left < 0:
                    total_passed_cars += 1
            else:
                index = abs(time_left) - free_window
                print(f"A crash happened!\n{current_car} was hit at {current_car[-index]}.")
                crash = True
                break
    else:
        cars.append(car)

if not crash:
    print(f"Everyone is safe.\n{total_passed_cars} total cars passed the crossroads.")