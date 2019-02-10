

from main import mongo_db
from global_helpers.response import internal_response


class ContactsHandler:
    @staticmethod
    def add_contact(user_id, contact_id):
        # Verify if the contact exists
        # Verify if the user already has the contact

        user_obj = mongo_db.users.find_one({'user_id': user_id})
        
        if mongo_db.users.find_one({'user_id': contact_id}) != None:
            if not any(contact_id for contact in user_obj['contacts']):
                mongo_db.users.update({'user_id': user_id}, {'$push': {'contacts': contact_id}})

                return internal_response(status="success", message="The contact has been added")
            else:
                return internal_response(status="error", message="The contact already exists")
        return internal_response(status="error", message="Unkown user id")

        
    @staticmethod
    def delete_contact(user_id, contact_id):
        user_obj = mongo_db.users.find_one({'user_id': user_id})

        if user_obj != None:
            if any(contact_id for contact in user_obj['contacts']):
                new_list = user_obj['contacts']
                new_list.remove(contact_id)

                mongo_db.users.update({'user_id': user_id}, {'$set': {'contacts': new_list}})

                return internal_response(status="success", message="The contact has been deleted")
            else:
                return internal_response(status="success", message="The contact does not exists")
        return internal_response(status="error", message="Unknown user id")

    @staticmethod
    def get_contacts(user_id):
        user_obj = mongo_db.users.find_one({'user_id': user_id})

        if user_obj != None:
            return internal_response(status="success", message="Retrieved contacts", data=user_obj['contacts'])
        return internal_response(status="success", message="Unknown user id")