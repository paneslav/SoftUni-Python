from collections import deque

bullet_price = int(input())
bullets_capacity = int(input())
bullets_stack = [int(x) for x in input().split()]
locks_queue = deque([int(x) for x in input().split()])
value_of_intelligence = int(input())

fired_bullets = 0

while bullets_stack and locks_queue:
    current_bullet = bullets_stack.pop()
    fired_bullets += 1
    current_lock = locks_queue[0]

    if current_bullet <= current_lock:
        locks_queue.popleft()
        print(f"Bang!")
    else:
        print(f"Ping!")

    if fired_bullets % bullets_capacity == 0 and bullets_stack:
        print(f"Reloading!")


if not locks_queue:
    print(f"{len(bullets_stack)} bullets left. Earned ${value_of_intelligence - (fired_bullets * bullet_price)}")
else:
    print(f"Couldn't get through. Locks left: {len(locks_queue)}")