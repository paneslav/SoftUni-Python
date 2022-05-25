n = int(input())

is_Pure = True

for _ in range(n):
    word = input()

    for i in range(len(word)):
        if ord(word[i]) == 95 or ord(word[i]) == 46 or ord(word[i]) == 44:
            is_Pure = False

    if is_Pure:
        print(f"{word} is pure.")
    else:
        print(f"{word} is not pure!")

    is_Pure = True