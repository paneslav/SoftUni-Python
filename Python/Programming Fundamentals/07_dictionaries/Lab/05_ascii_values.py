characters_list = input().split(', ')

ascii_dict = {char: ord(char) for char in characters_list}

print(ascii_dict)