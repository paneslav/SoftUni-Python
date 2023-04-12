class Table:
    TOTAL_TABLES = 30

    def __init__(self, number):
        self.number = number
        self.orders = []

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if not 1 <= value <= self.TOTAL_TABLES:
            raise ValueError(f"Table number out of range.")

        self.__number = value
