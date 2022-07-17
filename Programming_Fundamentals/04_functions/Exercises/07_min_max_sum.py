def min_max_sum(a):
    print(f"The minimum number is {min(a)}")
    print(f"The maximum number is {max(a)}")
    print(f"The sum number is: {sum(a)}")


numbers = list(map(int, input().split()))

min_max_sum(numbers)