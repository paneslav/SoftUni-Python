from collections import deque

seat_matches = []
rotations = 0
free_sits = input().split(', ')
# print(free_sits)
first_sequence = deque([int(x) for x in input().split(", ")])
second_sequence = [int(x) for x in input().split(", ")]

while len(seat_matches) != 3 and rotations != 10:
    rotations += 1
    first_num = first_sequence.popleft()
    second_num = second_sequence.pop()

    char_combination = chr(first_num + second_num)
    first_combination = f'{first_num}{char_combination}'
    second_combination = f'{second_num}{char_combination}'

    if first_combination not in free_sits and second_combination not in free_sits:
        first_sequence.append(first_num)
        second_sequence.insert(0, second_num)
        continue

    if first_combination in seat_matches or second_combination in seat_matches:
        continue

    if first_combination in free_sits:
        seat_matches.append(first_combination)
        continue

    if second_combination in free_sits:
        seat_matches.append(second_combination)


print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations}")
