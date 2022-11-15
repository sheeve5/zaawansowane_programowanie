from flask_restful import Resource
import csv
from classes.Tag import Tag
from classes.utils import serialize, get_int


class TagResource(Resource):
    def get(self):
        tags = get_tags()
        ret = serialize(tags)
        return ret


def get_tags():
    tags: list[Tag] = []
    with open('data/tags.csv', newline='', encoding='UTF-8') as file:
        file.readline()
        reader = csv.reader(file)
        for row in reader:
            user_id = get_int(row[0])
            movie_id = get_int(row[1])
            tag_text = row[2]
            timestamp = get_int(row[3])

            tag = Tag(user_id, movie_id, tag_text, timestamp)
            tags.append(tag)
    return tags
