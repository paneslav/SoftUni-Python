widht = int(input())
lenght = int(input())
height = int(input())

total_space = widht * lenght * height
space_taken = 0

while True:
    n = input()

    if n == "Done":
        print(f"{abs(total_space-space_taken)} Cubic meters left.")
        break

    meters = int(n)
    space_taken += meters

    if space_taken > total_space:
        print(f"No more free space! You need {abs(space_taken-total_space)} Cubic meters more.")
        break