n = int(input())

odd_set = set()
even_set = set()

for i in range(1, n + 1):
    name = input()

    current_sum = 0

    for char in name:
        current_sum += ord(char)

    current_sum //= i

    if current_sum % 2 == 0:
        even_set.add(current_sum)
    else:
        odd_set.add(current_sum)

if sum(odd_set) == sum(even_set):
    print(', '.join([str(x) for x in odd_set.union(even_set)]))
elif sum(odd_set) > sum(even_set):
    print(', '.join([str(x) for x in odd_set.difference(even_set)]))
else:
    print(', '.join([str(x) for x in odd_set.symmetric_difference(even_set)]))