from food.item import Item


class MainDish(Item):
    BASE_MULT = 1

    @property
    def cals(self):
        return self.grams * self.BASE_MULT

    def __str__(self):
        msg = [f"Информация за продукт: {self.name}", f"Грамаж: {self.grams}", f"Калории: {self.cals:.2f}"]
        return "\n".join(msg)