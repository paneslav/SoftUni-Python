word_to_remove = input()
string_to_manipulate = input()

while word_to_remove in string_to_manipulate:
    string_to_manipulate = string_to_manipulate.replace(word_to_remove, '')

print(string_to_manipulate)