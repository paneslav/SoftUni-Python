n = int(input())

cars_in_parking_lot = set()

for i in range(n):
    direction, plate_number = input().split(', ')

    if direction == 'IN':
        cars_in_parking_lot.add(plate_number)
    else:
        if plate_number in cars_in_parking_lot:
            cars_in_parking_lot.remove(plate_number)

if cars_in_parking_lot:
    print('\n'.join(cars_in_parking_lot))
else:
    print(f"Parking Lot is Empty")