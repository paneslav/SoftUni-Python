from project.animal import Animal


class Tiger(Animal):
    DEFAULT_MONEY_FOR_CARE = 45

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, self.DEFAULT_MONEY_FOR_CARE)