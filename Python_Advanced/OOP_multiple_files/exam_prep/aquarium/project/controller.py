from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    VALID_AQUARIUMS = ["FreshwaterAquarium", "SaltwaterAquarium"]
    VALID_DECORATIONS = ["Plant", "Ornament"]
    VALID_FISHES = ["FreshwaterFish", "SaltwaterFish"]

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.VALID_AQUARIUMS:
            return "Invalid aquarium type."

        if aquarium_type == "FreshwaterAquarium":
            aquarium = FreshwaterAquarium(aquarium_name)
        elif aquarium_type == "SaltwaterAquarium":
            aquarium = SaltwaterAquarium(aquarium_name)

        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in self.VALID_DECORATIONS:
            return "Invalid decoration type."

        if decoration_type == "Plant":
            decoration = Plant()
        elif decoration_type == "Ornament":
            decoration = Ornament()

        self.decorations_repository.decorations.append(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):

        decoration = self.decorations_repository.find_by_type(decoration_type)
        aquarium = self.__find_aqua_by_name(aquarium_name)

        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."

        if aquarium is None:
            return

        aquarium.decorations.append(decoration)
        self.decorations_repository.decorations.remove(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        aquarium = self.__find_aqua_by_name(aquarium_name)
        if fish_type not in self.VALID_FISHES:
            return f"There isn't a fish of type {fish_type}."

        if aquarium is None:
            return

        if fish_type == "FreshwaterFish":
            fish = FreshwaterFish(fish_name, fish_species, price)
        else:
            fish = SaltwaterFish(fish_name, fish_species, price)

        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__find_aqua_by_name(aquarium_name)
        return aquarium.feed()

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__find_aqua_by_name(aquarium_name)
        value = 0

        for deco in aquarium.decorations:
            value += deco.price

        for fish in aquarium.fish:
            value += fish.price

        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        return "\n".join([str(a) for a in self.aquariums])

    def __find_aqua_by_name(self, name):
        aqua = next(filter(lambda a: a.name == name, self.aquariums), None)
        return aqua
