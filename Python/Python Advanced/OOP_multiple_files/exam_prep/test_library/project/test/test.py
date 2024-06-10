from unittest import TestCase, main

from project.library import Library


class TestLibrary(TestCase):

    def setUp(self) -> None:
        self.library = Library("Test")
        self.books_by_author = {"TA1": ["TT1"], "TA2": ["TT2"]}
        self.readers = {"TR1": [{"TA1": "TT1"}, {"TA2": "TT2"}]}

    def test_correct_initialisation(self):
        self.assertEqual("Test", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_empty_string_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ""

        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_book_author_not_present_expect_add_author(self):
        self.library.add_book("TA1", "TT1")

        self.assertEqual({"TA1": ["TT1"]}, self.library.books_by_authors)

    def test_add_book_title_not_present_expect_add_title(self):
        self.library.books_by_authors = {"TA1": ["TT1"]}

        self.library.add_book("TA1", "TT2")

        self.assertEqual({"TA1": ["TT1", "TT2"]}, self.library.books_by_authors)

    def test_add_book_title_present_expect_nothing(self):
        self.library.books_by_authors = {"TA1": ["TT1"]}
        self.library.add_book("TA1", "TT1")

        self.assertEqual({"TA1": ["TT1"]}, self.library.books_by_authors)

    def test_add_reader_already_present_return_message(self):
        self.library.readers = self.readers
        result = self.library.add_reader("TR1")
        expected_result = "TR1 is already registered in the Test library."

        self.assertEqual(expected_result, result)

    def test_add_reader_not_present_expect_add_reader(self):
        self.library.add_reader("Ivan")

        self.assertEqual({"Ivan": []}, self.library.readers)

    def test_rent_book_reader_not_in_library_return_message(self):
        result = self.library.rent_book("TR1", "TA1", "TT1")
        expected_result = "TR1 is not registered in the Test Library."

        self.assertEqual(expected_result, result)

    def test_rent_book_author_not_present_in_library_return_message(self):
        self.library.readers = self.readers
        result = self.library.rent_book("TR1", "TA1", "TT1")
        expected_result = "Test Library does not have any TA1's books."

        self.assertEqual(expected_result, result)

    def test_rent_book_author_does_not_have_book_return_message(self):
        self.library.readers = self.readers
        self.library.books_by_authors = self.books_by_author
        result = self.library.rent_book("TR1", "TA1", "TT2")
        expected_result = """Test Library does not have TA1's "TT2"."""

        self.assertEqual(expected_result, result)

    def test_rent_book_expect_success(self):
        self.library.books_by_authors = self.books_by_author
        self.library.readers = {"TR1": []}
        self.library.rent_book("TR1", "TA1", "TT1")

        self.assertEqual({"TR1": [{"TA1": "TT1"}]}, self.library.readers)
        self.assertEqual({"TA1": [], "TA2": ["TT2"]}, self.library.books_by_authors)


if __name__ == "__main__":
    main()
