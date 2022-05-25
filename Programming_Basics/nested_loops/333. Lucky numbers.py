n = int(input())
is_lucky = False
first_sum = 0
second_sum = 0

for i in range(1, 10):
    for x in range(1, 10):
        for y in range(1, 10):
            for z in range(1, 10):
                first_sum = i + x
                second_sum = y + z

                if first_sum == second_sum and n % first_sum == 0:
                    is_lucky = True

                if is_lucky:
                    print(f"{i}{x}{y}{z}", end=" ")
                    first_sum = 0
                    second_sum = 0
                    is_lucky = False


