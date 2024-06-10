n = int(input())

parking_spots = {}

for _ in range(n):
    command = input().split()

    if command[0] == 'register':
        name = command[1]
        plate = command[2]

        if name not in parking_spots:
            parking_spots[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate}")
    elif command[0] == 'unregister':
        name = command[1]

        if name not in parking_spots:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            parking_spots.pop(name)

for user in parking_spots:
    print(f"{user} => {parking_spots[user]}")