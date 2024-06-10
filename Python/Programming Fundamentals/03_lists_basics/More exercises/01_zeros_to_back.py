list_of_numbers = input().split(', ')


for number in list_of_numbers:
    if number == '0':
        list_of_numbers.remove('0')
        list_of_numbers.append('0')

print(f"[{', '.join(list_of_numbers)}]")
