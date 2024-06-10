import math

from project.computer_types.computer import Computer


class Laptop(Computer):
    AVAILABLE_CPUS = {
        'AMD Ryzen 9 5950X': 900,
        'Intel Core i9-11900H': 1050,
        'Apple M1 Pro': 1200
    }
    MAXIMUM_RAM = 64

    def configure_computer(self, processor: str, ram: int):
        if processor not in Laptop.AVAILABLE_CPUS:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")

        if not self.power_of_two(ram) or ram > Laptop.MAXIMUM_RAM:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")

        self.set_parts(processor, ram)

        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."
