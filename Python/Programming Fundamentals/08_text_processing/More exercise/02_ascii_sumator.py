start = input()
end = input()
user_input = input()

total_sum = 0

for char in user_input:
    if ord(start) < ord(char) < ord(end):
        total_sum += ord(char)

print(total_sum)