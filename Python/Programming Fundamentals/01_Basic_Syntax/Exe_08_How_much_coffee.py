coffee = 0

while True:

    command = input()
    lower_case = command.lower()

    if command == "END":
        break

    if lower_case != "coding" and command.lower() != "dog" and command.lower() != "cat" and command.lower() != "movie":
        continue

    if command.isupper():
        coffee += 2
    else:
        coffee += 1

if coffee <= 5:
    print(coffee)
else:
    print("You need extra sleep")