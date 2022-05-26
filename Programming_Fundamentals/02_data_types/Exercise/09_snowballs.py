n = int(input())

max_value = 0

best_weight = 0
best_time = 0
best_quality = 0

for i in range(n):
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight / time) ** quality

    if value > max_value:
        max_value = value
        best_weight = weight
        best_time = time
        best_quality = quality

print(f"{best_weight} : {best_time} = {max_value:.0f} ({best_quality})")