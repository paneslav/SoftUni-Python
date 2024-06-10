from abc import ABC, abstractmethod


class FormulaTeam(ABC):

    @abstractmethod
    def __init__(self, budget):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int):
        money_from_sponsor = 0

        for sponsor in self.sponsors:
            for key, value in self.sponsors[sponsor].items():
                if race_pos <= key:
                    money_from_sponsor += value
                    break

        revenue = money_from_sponsor - self.race_expenses
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
