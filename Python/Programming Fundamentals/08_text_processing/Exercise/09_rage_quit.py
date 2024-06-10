user_input = input()

string_to_repeat = ''
repetitions = ''
final_result = ''
counter = 0

start_at = 0

for index in range(len(user_input)):
    if not user_input[index].isdigit():
        string_to_repeat += user_input[index]
    else:
        for i in range(index, len(user_input)):
            if not user_input[i].isdigit():
                break
            repetitions += user_input[i]
        final_result += string_to_repeat.upper() * int(repetitions)
        string_to_repeat = ''
        repetitions = ''


print(f"Unique symbols used: {len(set(final_result))}")
print(final_result)