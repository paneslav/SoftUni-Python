from food.item import Item


class Soup(Item):

    def __str__(self):
        msg = [f"Информация за продукт: {self.name}", f"Грамаж: {self.grams}", f"Калории: 0"]
        return "\n".join(msg)
