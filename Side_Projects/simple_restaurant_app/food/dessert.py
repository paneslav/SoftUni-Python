from food.item import Item


class Dessert(Item):
    BASE_MULT = 3

    @property
    def cals(self):
        return self.grams * self.BASE_MULT

    def __str__(self):
        msg = [f"Информация за продукт: {self.name}", f"Грамаж: {self.grams}", f"Калории: {self.cals}"]
        return "\n".join(msg)