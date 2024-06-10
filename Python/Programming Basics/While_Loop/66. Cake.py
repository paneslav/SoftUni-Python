x = int(input())
y = int(input())

total_pieces = x*y
while True:
    num = input()

    if num == "STOP":
        print(f"{total_pieces} pieces are left.")
        break
    pieces = int(num)
    total_pieces -= pieces

    if total_pieces <= 0:
        print(f"No more cake left! You need {abs(total_pieces)} pieces more.")
        break