flattened_matrix = []

initial_lists = [x.strip() for x in input().split('|')]

initial_lists = reversed(initial_lists)

for item in initial_lists:
    flattened_matrix.extend([x for x in item.split()])

print(' '.join(flattened_matrix))