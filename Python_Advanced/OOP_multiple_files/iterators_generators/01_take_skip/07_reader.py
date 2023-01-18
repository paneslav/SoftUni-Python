def read_next(*args):
    for item in args:
        for i in item:
            yield i


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
