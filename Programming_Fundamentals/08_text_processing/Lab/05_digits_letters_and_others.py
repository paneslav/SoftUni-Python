def check_for_digits(user_input):
    final_result = ''
    for char in user_input:
        if char.isdigit():
            final_result += char
    return final_result


def check_for_letters(user_input):
    final_result = ''
    for char in user_input:
        if char.isalpha():
            final_result += char
    return final_result


def check_for_others(user_input):
    final_result = ''
    for char in user_input:
        if not char.isalpha() and not char.isdigit():
            final_result += char
    return final_result


user_input = input()
print(check_for_digits(user_input))
print(check_for_letters(user_input))
print(check_for_others(user_input))