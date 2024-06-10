from collections import deque

cups_queue = deque([int(x) for x in input().split()])
bottles_stack = [int(x) for x in input().split()]

water_wasted = 0
filled_cups = 0

while cups_queue and bottles_stack:
    current_cup = cups_queue[0]
    current_bottle = bottles_stack.pop()

    if current_bottle >= current_cup:
        water_wasted += current_bottle - current_cup
        cups_queue.popleft()
        filled_cups += 1
    else:
        current_cup -= current_bottle
        while current_cup > 0:
            current_bottle = bottles_stack.pop()
            if current_bottle >= current_cup:
                water_wasted += current_bottle - current_cup
                cups_queue.popleft()
                filled_cups += 1
                break
            else:
                current_cup -= current_bottle


if not cups_queue:
    bottles_left = [str(x) for x in bottles_stack]
    print(f"Bottles: {' '.join(bottles_left)}")
else:
    cups_left = [str(x) for x in cups_queue]
    print(f"Cups: {' '.join(cups_left)}")

print(f"Wasted litters of water: {water_wasted}")