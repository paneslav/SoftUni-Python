from food.item import Item


class Beverage(Item):
    BASE_MULT = 1.5

    @property
    def cals(self):
        return self.grams * self.BASE_MULT

    def __str__(self):
        msg = [f"Информация за продукт: {self.name}", f"Грамаж: {self.grams}", f"Калории: {self.cals}"]
        return "\n".join(msg)