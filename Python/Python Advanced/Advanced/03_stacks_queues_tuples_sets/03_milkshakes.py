from collections import deque

milkshakes = 0

chocolate_stack = [int(x) for x in input().split(', ')]
milk_queue = deque([int(x) for x in input().split(', ')])

while milkshakes < 5 and chocolate_stack and milk_queue:
    current_chocolate = chocolate_stack.pop()  # last chocolate
    current_milk = milk_queue.popleft()  # first milk cup

    if current_milk <= 0 and current_chocolate <= 0:
        continue

    if current_milk <= 0:
        chocolate_stack.append(current_chocolate)
        continue

    if current_chocolate <= 0:
        milk_queue.appendleft(current_milk)
        continue

    if current_milk == current_chocolate:
        milkshakes += 1
    else:
        milk_queue.append(current_milk)
        chocolate_stack.append(current_chocolate - 5)

if milkshakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")

if chocolate_stack:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate_stack])}")
else:
    print(f"Chocolate: empty")

if milk_queue:
    print(f"Milk: {', '.join([str(x) for x in milk_queue])}")
else:
    print(f"Milk: empty")
