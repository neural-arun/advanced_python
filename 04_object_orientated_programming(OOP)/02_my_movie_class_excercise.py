class Movies:
    def __init__(self,movie_name,movie_director):
        self.movie = movie_name
        self.director = movie_director

    def print_info(self):
        return (f"{self.movie} by {self.director}")

my_movie = Movies('The Matrix', 'Wachowski')


print(my_movie.movie)
print(my_movie.director)
print(my_movie.print_info())