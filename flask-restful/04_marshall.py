from flask import Flask, Blueprint, request
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser
from flask_restful import inputs
import re
from flask_restful import fields, marshal_with, marshal
from flask import make_response, current_app
from flask_restful.utils import PY3
from json import dumps

app = Flask(__name__)

api = Api(app)


@api.representation('application/json')
def output_json(data, code, headers=None):
    """Makes a Flask response with a JSON encoded body"""

    # data = {'user_id':1, 'name': 'itcast'}
    # 此处为自己添加***************
    if 'message' not in data:
        data = {
            'message': 'OK',
            'data': data
        }
    # data = {"message": "OK", "data": {'user_id':1, 'name': 'itcast'}}
    # **************************

    settings = current_app.config.get('RESTFUL_JSON', {})

    # If we're in debug mode, and the indent is not set, we set it to a
    # reasonable value here.  Note that this won't override any existing value
    # that was set.  We also set the "sort_keys" value.
    if current_app.debug:
        settings.setdefault('indent', 4)
        settings.setdefault('sort_keys', not PY3)

    # always end the json dumps with a new line
    # see https://github.com/mitsuhiko/flask/pull/1262
    dumped = dumps(data, **settings) + "\n"

    resp = make_response(dumped, code)
    resp.headers.extend(headers or {})
    return resp


class User(object):
    def __init__(self, user_id, name, age):
        self.user_id = user_id
        self.name = name
        self.age = age

# 声明需要序列化处理的字段
resoure_fields = {
        'user_id': fields.Integer,
        'name': fields.String
    }

#


class Demo1Resource(Resource):
    @marshal_with(resoure_fields, envelope='data1')
    def get(self):
        user = User(1, 'itcast', 12)
        return user


class Demo2Resource(Resource):
    def get(self):
        user = User(1, 'itcast', 12)
        return marshal(user, resoure_fields, envelope='data2')


api.add_resource(Demo1Resource, '/demo1')


