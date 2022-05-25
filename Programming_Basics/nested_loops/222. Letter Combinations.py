first_letter = input()
last_letter = input()
letter_to_exclude = input()
counter = 0


for i in range(ord(first_letter), ord(last_letter) + 1):
    for y in range(ord(first_letter), ord(last_letter) + 1):
        for x in range(ord(first_letter), ord(last_letter) + 1):
            if chr(i) == letter_to_exclude or chr(y) == letter_to_exclude or chr(x) == letter_to_exclude:
                continue
            else:
                counter += 1
                print(f"{chr(i)}{chr(y)}{chr(x)}", end=" ")




print(counter)