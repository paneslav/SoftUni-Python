from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}  # author: []
        self.rented_books = {}  # {username: {book names: days to return}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        self.rented_books[user.username] = self.rented_books.get(user.username, {})
        if book_name in self.rented_books[user.username]:
            return f'The book "{book_name}" is already rented and will be available in {self.rented_books[user.username][book_name]} days!'

        if book_name in self.books_available[author]:
            user.books.append(book_name)  # add book to the user books
            self.books_available[author].remove(book_name)  # updates the available books
            self.rented_books[user.username][book_name] = days_to_return  # updates the rented books

            return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, user: User):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"

        user.books.remove(book_name)
        self.books_available[author].append(book_name)
        del self.rented_books[user.username][book_name]
