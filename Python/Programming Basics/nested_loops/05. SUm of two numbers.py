start = int(input())
end = int(input())
magic_number = int(input())
counter = 0
is_equal = False

for i in range(start, end + 1):
    if is_equal:
        break
    for y in range(start, end + 1):
        counter += 1
        if i + y == magic_number:
            print(f"Combination N:{counter} ({i} + {y} = {magic_number})")
            is_equal = True
            break

if not is_equal:
    print(f"{counter} combinations - neither equals {magic_number}")