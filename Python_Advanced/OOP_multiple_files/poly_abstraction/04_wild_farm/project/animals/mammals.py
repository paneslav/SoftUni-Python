from project.animals.animal import Mammal
from project.food import Meat, Fruit, Vegetable


class Mouse(Mammal):

    def make_sound(self):
        return f"Squeak"

    @property
    def allowed_food(self):
        return [Vegetable, Fruit]

    @property
    def gain_weight(self):
        return 0.1


class Dog(Mammal):

    def make_sound(self):
        return f"Woof!"

    @property
    def allowed_food(self):
        return [Meat]

    @property
    def gain_weight(self):
        return 0.4


class Cat(Mammal):

    def make_sound(self):
        return f"Meow"

    @property
    def allowed_food(self):
        return [Meat, Vegetable]

    @property
    def gain_weight(self):
        return 0.3


class Tiger(Mammal):

    def make_sound(self):
        return f"ROAR!!!"

    @property
    def allowed_food(self):
        return [Meat]

    @property
    def gain_weight(self):
        return 1.00
