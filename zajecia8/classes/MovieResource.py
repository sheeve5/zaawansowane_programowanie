from flask_restful import Resource
import csv
from classes.Movie import Movie
from classes.utils import serialize


class MovieResource(Resource):
    def get(self):
        movies = get_movies()
        ret = serialize(movies)
        return ret


def get_movies():
    movies: list[Movie] = []
    with open('data/movies.csv', newline='', encoding='UTF-8') as file:
        file.readline()

        reader = csv.reader(file)
        for row in reader:
            movie_id = int(row[0])
            movie_title = row[1]
            movie_genre = row[2]

            movie = Movie(movie_id, movie_title, movie_genre)
            movies.append(movie)
    return movies
