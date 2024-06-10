electrons = int(input())
electrons_list = []
counter = 1

while electrons > 0:

    electrons_to_fill = 2 * (counter ** 2)
    if electrons_to_fill > electrons:
        electrons_list.append(electrons)
        break
    electrons_list.append(electrons_to_fill)
    electrons -= electrons_to_fill

    counter += 1

print(electrons_list)