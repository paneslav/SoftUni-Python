start = int(input())
end = int(input())
is_special = False
even = False
odd = False
bigger = False
sum = False

first_odd = False
first_even = False
last_odd = False
last_even = False

for i in range(start, end + 1):
    for x in range(start, end + 1):
        for y in range(start, end + 1):
            for z in range(start, end + 1):

                if i > z:
                    bigger = True

                if (x + y) % 2 == 0:
                    sum = True

                if i % 2 == 0:
                    first_even = True
                else:
                    first_odd = True

                if z % 2 == 0:
                    last_even = True
                else:
                    last_odd = True

                if bigger and sum and (first_even != last_even or first_odd != last_odd):
                    print(f"{i}{x}{y}{z}", end=" ")

                bigger = False
                sum = False
                even = False
                odd = False
                first_even = False
                last_even = False
                first_odd = False
                last_odd = False