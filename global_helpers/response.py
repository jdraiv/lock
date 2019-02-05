
from sanic import json


def internal_response(status, message='None', data=None):
    return {'status': status, 'message': message}