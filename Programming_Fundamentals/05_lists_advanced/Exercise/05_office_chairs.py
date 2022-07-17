rooms = int(input())
total_free_chairs = 0
gameOn = False

for i in range(1, rooms + 1):
    chairs_visitors = input().split()

    chairs = len(chairs_visitors[0])
    visitors = int(chairs_visitors[1])
    total_free_chairs += chairs - visitors

    if visitors > chairs:
        print(f"{visitors-chairs} more chairs needed in room {i}")


if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")