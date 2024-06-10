from collections import deque

caffeine = [int(x) for x in input().split(', ')]
energy_drinks = deque([int(x) for x in input().split(', ')])

intake = 0

while caffeine and energy_drinks:
    current_caffeine = caffeine.pop()
    current_drink = energy_drinks.popleft()

    result = current_caffeine * current_drink

    if intake + result <= 300:
        intake += result
        continue
    else:
        energy_drinks.append(current_drink)
        intake -= 30
        if intake < 0:
            intake = 0

if energy_drinks:
    print(f"Drinks left: {', '.join([str(x) for x in energy_drinks])}")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {intake} mg caffeine.")
