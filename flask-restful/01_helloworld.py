from flask import Flask, Blueprint
from flask_restful import Resource, Api

app = Flask(__name__)

bp = Blueprint('bp', __name__)
#
# @bp.route('/')
# def view():
#     pass
#
# app.register_blueprint(bp)
#
# api = Api(app)
api = Api(bp)


class HelloWorldResource(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {'msg': 'post hello world'}


api.add_resource(HelloWorldResource, '/')

app.register_blueprint(bp)

