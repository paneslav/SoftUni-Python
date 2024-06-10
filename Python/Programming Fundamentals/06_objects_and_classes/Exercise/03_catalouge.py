class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []
        self.letter_list = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, letter):
        self.letter_list = [item for item in self.products if item.startswith(letter)]
        return self.letter_list

    def __repr__(self):
        sorted_list = sorted(self.products, key=lambda x: x)
        items_to_print = '\n'.join(sorted_list)
        return f"Items in the {self.name} catalogue:\n{items_to_print}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
