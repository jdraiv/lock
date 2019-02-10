

from sanic import Blueprint
from sanic.response import text, json
from global_helpers.request_json import request_json


contacts_module =  Blueprint('contacts_module')

# Helpers
from .helpers.ContactsHandler import ContactsHandler


@contacts_module.route('/add_contact', methods=['POST'])
async def add_contact(request):
    call_data = request_json(request, ['user_id', 'contact_id'])

    process_info = ContactsHandler.add_contact(call_data['data']['user_id'], call_data['data']['contact_id'])

    return json(process_info)


@contacts_module.route('/delete_contact', methods=['POST'])
async def delete_contact(request):
    call_data = request_json(request, ['user_id', 'contact_id'])

    process_info = ContactsHandler.delete_contact(call_data['data']['user_id'], call_data['data']['contact_id'])

    return json(process_info)

@contacts_module.route('/get_contacts', methods=['GET'])
async def get_contacts(request):
    call_data = request_json(request, ['user_id'])

    process_info = ContactsHandler.get_contacts(call_data['data']['user_id'])

    return json(process_info)


