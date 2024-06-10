from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    SIZE_INCREASE = 2
    HABITABLE_AREA = "SaltwaterAquarium"

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 5, price)