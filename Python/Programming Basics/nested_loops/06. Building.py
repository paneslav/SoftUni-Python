floors = int(input())
rooms_per_floor = int(input())

for i in range(floors, 0, -1):
    for y in range(0, rooms_per_floor):
        if floors == 1:
            print(f"L{i}{y}", end = " ")
        else:
            if floors == i:
                print(f"L{i}{y}", end = " ")
            else:
                if i % 2 == 0:
                    print(f"O{i}{y}", end = " ")
                else:
                    print(f"A{i}{y}", end = " ")

    print("")