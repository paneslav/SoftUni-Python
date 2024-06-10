letter = input()

word = ""
printIt = ""
n_count = False
c_count = False
o_count = False

while letter != "End":
    if (65 <= ord(letter) <= 90) or (97 <= ord(letter) <= 122):
        pass
    else:
        letter = input()
        continue

    if letter == "n":
        if n_count:
            word += letter
        n_count = True
    elif letter == "o":
        if o_count:
            word += letter
        o_count = True
    elif letter == "c":
        if c_count:
            word += letter
        c_count = True
    else:
        word += letter

    if n_count and c_count and o_count:
        printIt += f"{word} "
        word = ""
        n_count = False
        o_count = False
        c_count = False

    letter = input()



print(printIt)