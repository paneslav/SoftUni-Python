from project.animals.animal import Bird
from project.food import Meat, Seed, Fruit, Vegetable


class Owl(Bird):

    def make_sound(self):
        return f"Hoot Hoot"

    @property
    def allowed_food(self):
        return [Meat]

    @property
    def gain_weight(self):
        return 0.25


class Hen(Bird):

    def make_sound(self):
        return f"Cluck"

    @property
    def allowed_food(self):
        return [Meat, Vegetable, Fruit, Seed]

    @property
    def gain_weight(self):
        return 0.35
