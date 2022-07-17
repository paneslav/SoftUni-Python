contacts_dict = {}

n = 0
while True:
    command = input().split('-')
    if len(command) == 1:
        n = int(command[0])
        break

    name = command[0]
    number = command[1]

    contacts_dict[name] = number


for _ in range(n):
    command = input()
    if command in contacts_dict:
        print(f"{command} -> {contacts_dict[command]}")
    else:
        print(f"Contact {command} does not exist.")
