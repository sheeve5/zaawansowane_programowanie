from flask_restful import Resource
import csv
from classes.Link import Link
from classes.utils import serialize, get_int


class LinkResource(Resource):
    def get(self):
        links = get_links()
        ret = serialize(links)
        return ret


def get_links():
    links: list[Link] = []
    with open('data/links.csv', newline='', encoding='UTF-8') as file:
        file.readline()
        reader = csv.reader(file)
        for row in reader:
            movie_id = get_int(row[0])
            imdb_id = get_int(row[1])
            tmdb_id = get_int(row[2])

            link = Link(movie_id, imdb_id, tmdb_id)
            links.append(link)
    return links
