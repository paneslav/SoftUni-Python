clothes = list(map(int, input().split()))
rack_capacity = int(input())

current_capacity = 0

total_racks = 1

while clothes:
    current_cloth = clothes[-1]
    if current_capacity + current_cloth < rack_capacity:
        current_capacity += clothes.pop(-1)
    elif current_capacity + current_cloth == rack_capacity:
        current_capacity = rack_capacity
        clothes.pop(-1)
    else:
        current_capacity = clothes.pop(-1)
        total_racks += 1

print(total_racks)