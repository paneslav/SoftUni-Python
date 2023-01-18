from abc import ABC, abstractmethod

from project.validator import Validator


class Astronaut(ABC):
    BREATHE_AMOUNT = 10
    VALID_ASTRONAUTS = ["Biologist", "Geodesist", "Meteorologist"]

    @abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    def breathe(self):
        self.oxygen -= self.BREATHE_AMOUNT

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.is_string_empty(value, "Astronaut")
        self.__name = value

    def __str__(self):
        items = ", ".join([item for item in self.backpack]) if self.backpack else "none"
        result = [f"Name: {self.name}", f"Oxygen: {self.oxygen}", f"Backpack items: {items}"]

        return "\n".join(result)

# a1 = Astronaut(" ", 65)
