from collections import deque

client_queue = deque()

while True:
    customer = input()

    if customer == 'End':
        print(f"{len(client_queue)} people remaining.")
        break

    if customer == 'Paid':
        while client_queue:
            print(client_queue.popleft())
    else:
        client_queue.append(customer)