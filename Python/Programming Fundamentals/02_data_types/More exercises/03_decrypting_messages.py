key = int(input())
n = int(input())

word = ''

for i in range(n):
    word += chr(ord(input()) + key)

print(word)