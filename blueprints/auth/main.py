

from sanic.response import json, text
from sanic import Blueprint


auth_module = Blueprint('auth_module')

from main import keys

# Helpers

from global_helpers.response import internal_response
from global_helpers.request_json import request_json
from .helpers.CreateAcc import CreateAcc
from .helpers.LogAcc import LogAcc


@auth_module.route('/create_account', methods=['POST'])
async def create_account(request):

    call_data = request_json(request, ['user_id', 'password'])

    if call_data['valid_call']:
        if CreateAcc.valid_user_id(call_data['data']['user_id'], call_data['data']['password']):
            return json(internal_response(status="success", message="User created"))
        return json(internal_response(status="error", message="Username is not available"))
    else:
        return json(internal_response(status="success", message="Unknown error"))


@auth_module.route('/login', methods=['POST'])
async def log_user(request):

    call_data = request_json(request, ['user_id', 'password'])

    if call_data['valid_call']:
        if LogAcc.valid_credentials(call_data['data']['user_id'], call_data['data']['password']):
            return json(internal_response(status="success", message="Valid credentials"))
        return json(internal_response(status="error", message="Incorrect username or password"))
    else:
        return json(internal_response(status="success", message="Unknown user"))