days = int(input())
hours_per_day = int(input())

current_cost = 0
total_cost = 0

for i in range(1, days + 1):
    for x in range(1, hours_per_day + 1):
        if i % 2 == 0 and x % 2 != 0:
            current_cost += 2.50
        elif i % 2 != 0 and x % 2 == 0:
            current_cost += 1.25
        else:
            current_cost += 1
    total_cost += current_cost
    print(f"Day: {i} - {current_cost:.2f} leva")
    current_cost = 0
print(f"Total: {total_cost:.2f} leva")
