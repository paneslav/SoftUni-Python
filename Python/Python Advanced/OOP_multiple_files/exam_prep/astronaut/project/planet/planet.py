from project.validator import Validator


class Planet:

    def __init__(self, name: str):
        self.name = name
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.is_string_empty(value, "Planet")
        self.__name = value

# p = Planet("")