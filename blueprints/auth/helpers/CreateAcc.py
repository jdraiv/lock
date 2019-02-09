
import bcrypt

from main import mongo_db
from global_helpers.response import internal_response



class CreateAcc:
    @staticmethod
    def valid_user_id(user_id, password):
        # We verify if the username is available
        user_obj = mongo_db.users.find_one({'user_id': user_id})

        if user_obj == None and password != None:
            # encrypted_pw = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())

            return True
        return False

    @staticmethod
    def store_user(user_id, password):
        try:
            encrypted_pw = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())

            user_obj = {
                'user_id': user_id,
                'password': encrypted_pw,
                'chats': [],
                'contacts': [],
                'settings': {
                    'privacy': {"view_profile_picture": "Contacts", "view_status": "Contacts", "contact_me": "Contacts"},
                    'profile': {"picture": "", "status": ""}
                }
            }

            mongo_db.users.insert_one(user_obj)
            return True
        except:
            return False

    # Head method
    @staticmethod
    def attemp_user_creation(user_id, password):
        # 1. Verify if user is available
        # 2. Create user

        if CreateAcc.valid_user_id(user_id, password):
            # Create user
            if CreateAcc.store_user(user_id, password):
                return True
            else:
                return False
        else:
            # Error, username is not available
            return False
