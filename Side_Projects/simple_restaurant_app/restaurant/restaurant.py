from food.beverage import Beverage
from food.dessert import Dessert
from food.main_dish import MainDish
from food.salad import Salad
from food.soup import Soup
from restaurant.table import Table


class Restaurant:
    product_type_refs = {
        "салата": Salad,
        "супа": Soup,
        "основно ястие": MainDish,
        "десерт": Dessert,
        "напитка": Beverage
    }

    def __init__(self):
        self.menu = []
        self.occupied_tables = {}
        self.sales_info = {
            "Salad": {
                "name": "Салата",
                "count": 0,
                "profit": 0
            },
            "Soup": {
                "name": "Супа",
                "count": 0,
                "profit": 0
            },
            "MainDish": {
                "name": "Основно ястие",
                "count": 0,
                "profit": 0
            },
            "Dessert": {
                "name": "Десерт",
                "count": 0,
                "profit": 0
            },
            "Beverage": {
                "name": "Напитка",
                "count": 0,
                "profit": 0
            }
        }

    def add_product_to_menu(self, product_type, product_name, grams, price):
        product = self.product_type_refs[product_type](product_name, int(grams), float(price))
        self.menu.append(product)

    def make_order(self, table_number, *args):
        # check if table is instantiated
        if table_number not in self.occupied_tables:
            self.occupied_tables[table_number] = Table(int(table_number))

        # make orders for existing products
        for item in args:
            product = self.find_product_by_name(item)

            if not product:
                print("Item not found in menu!")
                continue

            product_type = product.__class__.__name__

            self.sales_info[product_type]["count"] += 1
            self.sales_info[product_type]["profit"] += product.price

            self.occupied_tables[table_number].orders.append(product)

    def show_stats(self):
        total_tables = f"Общо заети маси през деня: {len(self.occupied_tables)}"
        total_sales = f"Общо продажби: {self.get_total_sales()}"
        total_profit = self.get_total_sales_by_category()

        result = [total_tables, total_sales, "По категории:", total_profit]

        return "\n".join(result)

    def get_total_sales(self):
        total_sales = 0
        total_profit = 0

        for item in self.sales_info.values():
            total_sales += item["count"]
            total_profit += item["profit"]

        return f"{total_sales} – {total_profit:.2f}"

    def get_total_sales_by_category(self):
        result = []

        for item in self.sales_info.values():
            result.append(f" - {item['name']}: {item['count']} - {item['profit']:.2f}")

        return "\n".join(result)

    def find_product_by_name(self, product_name):
        return next(filter(lambda n: n.name == product_name, self.menu), None)
