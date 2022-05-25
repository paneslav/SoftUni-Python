x_cap = int(input())
y_cap = int(input())
max_pass = int(input())

A = chr(35)
B = chr(64)

A_in_int = ord(A)
B_in_int = ord(B)

x_current = 1
y_current = 1
to_End = False
counter = 0

for i in range(1, x_cap + 1):
    if to_End:
        break
    for y in range(1, y_cap + 1):
        print(f"{chr(A_in_int)}{chr(B_in_int)}{i}{y}{chr(B_in_int)}{chr(A_in_int)}|", end='')

        A_in_int += 1
        B_in_int += 1
        counter += 1

        if A_in_int > 55:
            A_in_int = ord(A)

        if B_in_int > 96:
            B_in_int = ord(B)

        if counter == max_pass:
            to_End = True
            break




