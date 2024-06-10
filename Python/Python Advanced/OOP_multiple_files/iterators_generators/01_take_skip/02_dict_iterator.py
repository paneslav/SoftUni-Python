class dictionary_iter:

    def __init__(self, dict_object):
        self.dict = list(dict_object.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.dict):
            raise StopIteration

        self.index += 1

        return self.dict[self.index - 1]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
