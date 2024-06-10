words_list = input().split()
palindrome_to_search = input().rstrip()

palindromes = [i for i in words_list if i == i[::-1]]

print(palindromes)
print(f"Found palindrome {words_list.count(palindrome_to_search)} times")