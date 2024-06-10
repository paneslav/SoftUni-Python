from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    BREATHE_AMOUNT = 5

    def __init__(self, name: str, oxygen: int = 70):
        super().__init__(name, oxygen)


# b = Biologist("", 65)