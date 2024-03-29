from abc import ABC, abstractmethod


class BaseAquarium(ABC):

    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    def calculate_comfort(self):
        total_comfort = 0
        for decoration in self.decorations:
            total_comfort += decoration.comfort

        return total_comfort

    def add_fish(self, fish):
        if self.capacity == 0:
            return "Not enough capacity."

        fish_type = fish.__class__.__name__
        aqua_type = self.__class__.__name__

        if fish.HABITABLE_AREA != aqua_type:
            return "Water not suitable."

        self.fish.append(fish)
        return f"Successfully added {fish_type} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        fed_count = 0
        for fish in self.fish:
            fish.eat()
            fed_count += 1

        return f"Fish fed: {fed_count}"

    def __str__(self):
        fishes = " ".join([fish.name for fish in self.fish]) if self.fish else "none"
        result = [f"{self.name}:", f"Fish: {fishes}", f"Decorations: {len(self.decorations)}",
                  f"Comfort: {self.calculate_comfort()}"]

        return "\n".join(result)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value
