import math

from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    AVAILABLE_CPUS = {
        'AMD Ryzen 7 5700G': 500,
        'Intel Core i5-12600K': 600,
        'Apple M1 Max': 1800
    }
    MAXIMUM_RAM = 128

    def configure_computer(self, processor: str, ram: int):
        if processor not in DesktopComputer.AVAILABLE_CPUS:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")

        if not self.power_of_two(ram) or ram > DesktopComputer.MAXIMUM_RAM:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        self.set_parts(processor, ram)

        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."
