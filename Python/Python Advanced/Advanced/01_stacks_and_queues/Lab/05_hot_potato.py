from collections import deque

kids = deque(input().split())
toss_count = int(input())

counter = 0

while len(kids) != 1:
    counter += 1
    kid = kids.popleft()
    if counter != toss_count:
        kids.append(kid)
    else:
        print(f"Removed {kid}")
        counter = 0

print(f"Last is {kids[0]}")