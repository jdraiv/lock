

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

    process_info = CreateAcc.attemp_user_creation(call_data['data']['user_id'], call_data['data']['password'])

    return json(process_info)

@auth_module.route('/login', methods=['POST'])
async def log_user(request):

    call_data = request_json(request, ['user_id', 'password'])

    process_info = LogAcc.valid_credentials(call_data['data']['user_id'], call_data['data']['password'])

    return json(process_info)