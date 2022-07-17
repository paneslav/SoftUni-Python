from collections import defaultdict

resources_dict = defaultdict(int)
current_index = 1

while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())

    resources_dict[resource] += quantity

result_to_print = [f'{resource} -> {resources_dict[resource]}' for resource in resources_dict]
print('\n'.join(result_to_print))