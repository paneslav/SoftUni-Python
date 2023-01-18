import math
from abc import ABC, abstractmethod


class Computer(ABC):
    AVAILABLE_CPUS = {}

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @staticmethod
    def power_of_two(ram):
        result = math.log2(ram)
        return math.ceil(result) == math.floor(result)

    @abstractmethod
    def configure_computer(self, processor: str, ram: int):
        pass

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '':
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == '':
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"

    def set_parts(self, processor: str, ram: int):
        self.processor = processor
        self.ram = ram
        self.price += self.AVAILABLE_CPUS[processor]
        self.price += int(math.log2(ram)) * 100
