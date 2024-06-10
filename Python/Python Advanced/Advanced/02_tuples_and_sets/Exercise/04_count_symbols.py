text = input()

occurrence = {}

for char in text:
    if char not in occurrence:
        occurrence[char] = 0

    occurrence[char] += 1

for key, value in sorted(occurrence.items()):
    print(f"{key}: {value} time/s")