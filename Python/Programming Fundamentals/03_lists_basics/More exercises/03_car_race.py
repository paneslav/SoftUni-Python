first_racer_lap = 0
second_racer_lap = 0

times = input().split()

middle_index = len(times)//2

first_racer_times = times[:middle_index]
second_racer_times = times[middle_index + 1:]
second_racer_times.reverse()

for element in first_racer_times:

    first_racer_lap += float(element)

    if element == "0":
        first_racer_lap *= 0.8


for element in second_racer_times:

    second_racer_lap += float(element)

    if element == "0":
        second_racer_lap *= 0.8

if first_racer_lap < second_racer_lap:
    print(f"The winner is left with total time: {first_racer_lap:.1f}")
else:
    print(f"The winner is right with total time: {second_racer_lap:.1f}")