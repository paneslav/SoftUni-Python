strings_to_modify = input().split()

total_sum = 0

for item in strings_to_modify:
    first_letter = item[0]
    last_letter = item[-1]
    number = int(item[1:-1])

    if first_letter.isupper():
        number /= (ord(first_letter) - 64)
    else:
        number *= (ord(first_letter) - 96)

    if last_letter.isupper():
        number -= (ord(last_letter) - 64)
    else:
        number += (ord(last_letter) - 96)

    total_sum += number

print(f"{total_sum:.2f}")