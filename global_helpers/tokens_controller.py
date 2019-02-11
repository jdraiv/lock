
from main import keys

import jwt
import pyrtk


def create_jwt(user_id):
    return jwt.encode({'user_id': user_id}, keys['JWT_KEY'], algorithm="HS256").decode('utf-8')


def create_rtk(user_id):
    return pyrtk.create_token(user_id, keys['RTK_KEY'])


def decode_jwt(user_id):
    pass


def decode_rtk(user_id):
    pass


