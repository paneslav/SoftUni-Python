class ProductRepository():

    products = []

    def add(self, product):
        if product not in self.products:
            self.products.append(product)

    def find(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)

    def __repr__(self):
        result = [f'{product.name}: {product.quantity}' for product in self.products]
        return '\n'.join(result)
