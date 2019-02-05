

from sanic.response import json, text
from sanic import Blueprint


auth_module = Blueprint('auth_module')

from main import keys

# Helpers

from global_helpers.response import internal_response
from .helpers.CreateAcc import CreateAcc


@auth_module.route('/create_account', methods=['POST'])
async def create_account(request):
    user_id = request.json['user_id']
    password = request.json['password']

    if CreateAcc.valid_user_id(user_id, password):
        return json(internal_response(status="success", message="User created"))
    return json(internal_response(status="error", message="Username is not available"))


@auth_module.route('/log_user', methods=['POST'])
async def log_user(request):
    pass