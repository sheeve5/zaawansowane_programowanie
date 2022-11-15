from flask_restful import Resource
import csv
from classes.Rating import Rating
from classes.utils import serialize, get_int


class RatingResource(Resource):
    def get(self):
        ratings = get_ratings()
        ret = serialize(ratings)
        return ret


def get_ratings():
    ratings: list[Rating] = []
    with open('data/ratings.csv', newline='', encoding='UTF-8') as file:
        file.readline()
        reader = csv.reader(file)
        for row in reader:
            user_id = get_int(row[0])
            movie_id = get_int(row[1])
            score = row[2]
            timestamp = get_int(row[3])

            rating = Rating(user_id, movie_id, score, timestamp)
            ratings.append(rating)
    return ratings
