numbers = [float(x) for x in input().split()]

occurrence_count = {}

for number in numbers:
    if number not in occurrence_count:
        occurrence_count[number] = 0

    occurrence_count[number] += 1

for key, value in occurrence_count.items():
    print(f"{key:.1f} - {value} times")