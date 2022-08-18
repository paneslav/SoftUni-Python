from collections import deque

food = int(input())

orders = deque(list(map(int, input().split())))

print(max(orders))

while orders:
    food_needed = orders[0]
    if food_needed <= food:
        food -= orders.popleft()
    else:
        break

if len(orders) != 0:
    print(f"Orders left: {' '.join(str(x) for x in orders)}")
else:
    print(f"Orders complete")
