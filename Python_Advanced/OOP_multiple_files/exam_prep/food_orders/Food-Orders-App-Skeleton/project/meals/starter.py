from project.meals.meal import Meal


class Starter(Meal):

    def __init__(self, name: str, price: float, quantity=60):
        super().__init__(name, price, quantity)

    def __str__(self):
        return f"Starter {self.name}: {self.price:.2f}lv/piece"
