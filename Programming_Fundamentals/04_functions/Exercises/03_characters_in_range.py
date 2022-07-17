def characters_inbetween(a, b):
    for i in range(ord(a) + 1, ord(b)):
        print(chr(i), end=' ')


start = input()
end = input()

characters_inbetween(start, end)