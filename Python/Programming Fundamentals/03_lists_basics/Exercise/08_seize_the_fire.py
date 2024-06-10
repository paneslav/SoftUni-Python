fire = input().split('#')
water = int(input())

cell = int
total_fire = 0
effort = 0

print("Cells:")  # prints first row "Cells:"

for element in fire:

    if element[0] == 'H':

        cell = int(element[7:])

        if 81 <= cell <= 125 and water >= cell:

            water -= cell
            total_fire += cell
            effort += cell * 0.25
            print(f" - {cell}")

    elif element[0] == 'M':

        cell = int(element[9:])

        if 51 <= cell <= 80 and water >= cell:

            water -= cell
            total_fire += cell
            effort += cell * 0.25
            print(f" - {cell}")

    elif element[0] == 'L':

        cell = int(element[6:])

        if 1 <= cell <= 50 and water >= cell:
            water -= cell
            total_fire += cell
            effort += cell * 0.25
            print(f" - {cell}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")