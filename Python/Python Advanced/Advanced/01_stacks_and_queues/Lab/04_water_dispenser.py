from collections import deque

water_quantity = int(input())
customers_queue = deque()

while True:
    customer = input()
    if customer == 'Start':
        break

    customers_queue.append(customer)

while True:
    command = input().split()

    if command[0] == 'End':
        print(f"{water_quantity} liters left")
        break

    if command[0] == 'refill':
        liters_to_add = int(command[-1])
        water_quantity += liters_to_add
    else:
        liters_needed = int(command[0])
        current_customer = customers_queue.popleft()
        if water_quantity >= liters_needed:
            print(f"{current_customer} got water")
            water_quantity -= liters_needed
        else:
            print(f"{current_customer} must wait")