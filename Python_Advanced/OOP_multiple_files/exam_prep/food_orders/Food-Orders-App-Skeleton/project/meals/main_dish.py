from project.meals.meal import Meal


class MainDish(Meal):

    def __init__(self, name: str, price: float, quantity=50):
        super().__init__(name, price, quantity)

    def __str__(self):
        return f"Main Dish {self.name}: {self.price:.2f}lv/piece"