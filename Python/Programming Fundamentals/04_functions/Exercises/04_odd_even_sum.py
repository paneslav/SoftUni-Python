def odd_even_position_sum(a):
    odd_sum = 0
    even_sum = 0
    for i in range(len(a)):
        if int(a[i]) % 2 == 0:
            even_sum += int(a[i])
        else:
            odd_sum += int(a[i])
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


number = input()
odd_even_position_sum(number)