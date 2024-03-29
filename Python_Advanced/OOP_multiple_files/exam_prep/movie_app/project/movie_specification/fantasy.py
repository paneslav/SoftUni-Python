from project.movie_specification.movie import Movie
from project.user import User


class Fantasy(Movie):
    _age_restriction = 6

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = 6):
        super().__init__(title, year, owner, age_restriction)
