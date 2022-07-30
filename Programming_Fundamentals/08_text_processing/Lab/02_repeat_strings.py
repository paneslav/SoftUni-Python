user_input = input().split()

final_output = ''

for item in user_input:
    final_output += item * len(item)

print(final_output)