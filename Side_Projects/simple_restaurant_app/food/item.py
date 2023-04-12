from abc import ABC, abstractmethod


class Item(ABC):

    def __init__(self, name, grams, price):
        self.name = name
        self.grams = grams
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not all(x.isalpha() or x.isspace() for x in value):
            raise ValueError("Invalid product name!")

        self.__name = value

    @property
    def grams(self):
        return self.__grams

    @grams.setter
    def grams(self, value):
        if not 0 <= int(value) <= 1000:
            raise ValueError("Grams are not in the range of 0 to 1000.")

        self.__grams = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not 0 <= float(value) <= 100:
            raise ValueError("Price is not in the range of 0 to 100.")

        self.__price = value

    @abstractmethod
    def __str__(self):
        pass
