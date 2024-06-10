from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    VALID_MEALS = ["Starter", "MainDish", "Dessert"]
    RECEIPT_NO = 1

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        if self.find_client(client_phone_number):
            raise Exception("The client has already been registered!")

        self.clients_list.append(Client(client_phone_number))

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ not in FoodOrdersApp.VALID_MEALS:
                continue

            self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        result = []
        for meal in self.menu:
            result.append(meal.details())

        return "\n".join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        client = self.find_client(client_phone_number)

        if not client:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        self.check_menu(meal_names_and_quantities.keys())
        self.check_quantity(meal_names_and_quantities)

        for meal_name, quant in meal_names_and_quantities.items():
            meal = self.find_meal_in_menu(meal_name)

            meal.quantity -= quant
            client.bill += meal.price * quant
            client.shopping_cart.append(meal)
            client.ordered_items[meal_name] = quant

        return f"Client {client_phone_number} successfully ordered {', '.join([meal.name for meal in client.shopping_cart])} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.find_client(client_phone_number)

        if len(client.shopping_cart) == 0:
            raise Exception(f"There are no ordered meals!")

        for meal, quant in client.ordered_items.items():
            m = self.find_meal_in_menu(meal)
            m.quantity += quant

        client.shopping_cart = []
        client.ordered_items = {}
        client.bill = 0

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.find_client(client_phone_number)

        if len(client.shopping_cart) == 0:
            raise Exception(f"There are no ordered meals!")

        result = f"Receipt #{FoodOrdersApp.RECEIPT_NO} with total amount of {client.bill:.2f} was successfully paid for {client_phone_number}."

        client.shopping_cart = []
        client.ordered_items = {}
        client.bill = 0.0
        FoodOrdersApp.RECEIPT_NO += 1

        return result

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    def find_client(self, phone_number):
        client = next(filter(lambda c: c.phone_number == phone_number, self.clients_list), None)

        return client

    def find_meal_in_menu(self, meal):
        meal = next(filter(lambda m: m.name == meal, self.menu), None)

        return meal

    def check_menu(self, meals):
        for item in meals:
            meal = self.find_meal_in_menu(item)
            if not meal:
                raise Exception(f"{item} is not on the menu!")

    def check_quantity(self, items):
        for meal_name, quant in items.items():
            meal = self.find_meal_in_menu(meal_name)
            if meal.quantity < quant:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")

