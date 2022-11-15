from flask import Flask, request
from flask_restful import Resource, Api
from classes.MovieResource import MovieResource
from classes.LinkResource import LinkResource
from classes.RatingResource import RatingResource
from classes.TagResource import TagResource

app = Flask(__name__)
api = Api(app)

api.add_resource(MovieResource, '/movies')
api.add_resource(LinkResource, '/links')
api.add_resource(RatingResource, '/ratings')
api.add_resource(TagResource, '/tags')

app.run(debug=True)
