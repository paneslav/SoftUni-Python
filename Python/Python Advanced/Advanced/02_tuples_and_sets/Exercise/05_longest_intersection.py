n = int(input())

longest_intersection = 0

winner = set()

for _ in range(n):
    ranges = input().split('-')

    first_start, first_end = ranges[0].split(',')
    second_start, second_end = ranges[-1].split(',')

    first_range = set(range(int(first_start), int(first_end) + 1))
    second_range = set(range(int(second_start), int(second_end) + 1))

    current_intersection_length = len(first_range & second_range)

    if current_intersection_length > longest_intersection:
        longest_intersection = current_intersection_length
        winner = first_range & second_range

print(f"Longest intersection is [{', '.join(str(x) for x in winner)}] with length {longest_intersection}")