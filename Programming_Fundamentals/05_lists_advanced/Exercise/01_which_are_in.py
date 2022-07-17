searched_strings = input().split(', ')
words_to_search_in = input().split(', ')

result = []

for item in searched_strings:
    for word in words_to_search_in:
        if item in word and item not in result:
            result.append(item)

print(result)