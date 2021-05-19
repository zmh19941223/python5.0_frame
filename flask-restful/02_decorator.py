from flask import Flask, Blueprint, request
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)


def decorator1(func):
    def wrapper(*args, **kwargs):
        print('decorator1')
        return func(*args, **kwargs)

    return wrapper


def decorator2(func):
    def wrapper(*args, **kwargs):
        print('decorator2')
        return func(*args, **kwargs)

    return wrapper


class DemoResource(Resource):
    method_decorators = [decorator1, decorator2]

    # for dec in method_decorators:
    #      func = dec(fuc)
    #
    #   get = decorator1(get)
    #   get = decorator2(get)


    # @decorator2
    # @decorator1
    # def get

#     def decorator1(func):

#         def wrapper(*args, **kwargs):
#             print('decorator1')
#             return func(*args, **kwargs)
#
#         return wrapper
#
#     def decorator2(func):
#         def wrapper(*args, **kwargs):
#             print('decorator2')
#             return func(*args, **kwargs)
#         return wrapper
#
# get->  decorator2(  decorator1(get)     )
#     ->  decorator2(   decorator1->wrapper    )
#     ->  decorator2-> wrapper
#
# get() = decorator2-> wrapper()
#                 decorator1->wrapper()
#                     get()
    def get(self):
        return {'msg': 'get view'}

    def post(self):
        return {'msg': 'post view'}


api.add_resource(DemoResource, '/')


