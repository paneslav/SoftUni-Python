from project.meals.meal import Meal


class Dessert(Meal):

    def __init__(self, name: str, price: float, quantity=30):
        super().__init__(name, price, quantity)

    def __str__(self):
        return f"Dessert {self.name}: {self.price:.2f}lv/piece"