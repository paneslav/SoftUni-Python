from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):

    def setUp(self) -> None:
        self.cart = ShoppingCart("Staskata", 100)
        self.products = {
            "test": 30,
            "test2": 40,
            "test3": 40
        }

    def test_correct_initialisation(self):
        self.assertEqual("Staskata", self.cart.shop_name)
        self.assertEqual(100, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_shop_name_no_capital_letter_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "staskata"

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_shop_name_digit_in_name_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "Staskata1"

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_add_to_cart_item_costs_100_or_more_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("test", 100)

        self.assertEqual("Product test cost too much!", str(ve.exception))

    def test_add_to_cart_correct_expect_success(self):
        result = self.cart.add_to_cart("test", 50.0)

        self.assertEqual({"test": 50.0}, self.cart.products)
        self.assertEqual("test product was successfully added to the cart!", result)

    def test_remove_from_cart_book_not_present_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart("test")

        self.assertEqual("No product with name test in the cart!", str(ve.exception))

    def test_remove_from_cart_correct_expect_success(self):
        self.cart.products = self.products

        result = self.cart.remove_from_cart("test")

        self.assertEqual({"test2": 40, "test3": 40}, self.cart.products)
        self.assertEqual("Product test was successfully removed from the cart!", result)

    def test_add_dunder_method(self):
        self.cart.products = self.products
        other = ShoppingCart("Panev", 100)
        other.products = {
            "tt": 1
        }

        result = self.cart + other

        self.assertEqual("StaskataPanev", result.shop_name)
        self.assertEqual(200, result.budget)
        self.assertEqual({
            "test": 30,
            "test2": 40,
            "test3": 40,
            "tt": 1
        }, result.products)

    def test_buy_products_not_enough_money_raise_value_error(self):
        self.cart.products = self.products

        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()

        self.assertEqual("Not enough money to buy the products! Over budget with 10.00lv!", str(ve.exception))

    def test_buy_products_enough_money_expect_success(self):
        self.cart.products = {
            "test": 20,
            "test1": 30
        }

        result = self.cart.buy_products()

        self.assertEqual("Products were successfully bought! Total cost: 50.00lv.", result)


if __name__ == '__main__':
    main()
