from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        if self.find_user_by_username(username):
            raise Exception("User already exists!")

        self.users_collection.append(User(username, age))
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = self.find_user_by_username(username)

        if user is None:
            raise Exception("This user does not exist!")

        if movie.owner.username != user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        self.movies_collection.append(movie)
        user.movies_owned.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self.find_user_by_username(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner.username != user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for attrib, new_value in kwargs.items():
            if attrib == "title":
                movie.title = new_value
            elif attrib == "year":
                movie.year = new_value
            elif attrib == "age_restriction":
                movie.age_restriction = new_value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self.find_user_by_username(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner.username != user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        movie_title = movie.title
        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)

        return f"{username} successfully deleted {movie_title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.find_user_by_username(username)

        if movie.owner.username == user.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.find_user_by_username(username)

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        return '\n'.join(s.details() for s in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)))

    def __str__(self):
        output = ["All users: "]
        if not self.users_collection:
            output[0] += "No users."
        else:
            output[0] += ', '.join(u.username for u in self.users_collection)

        output.append("All movies: ")
        if not self.movies_collection:
            output[1] += "No movies."
        else:
            output[1] += ', '.join(u.title for u in self.movies_collection)

        return "\n".join(output)

    def find_user_by_username(self, username):
        user = next(filter(lambda u: u.username == username, self.users_collection), None)

        return user
