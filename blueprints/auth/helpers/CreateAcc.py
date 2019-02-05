
import bcrypt

from main import mongo_db
from global_helpers.response import internal_response



class CreateAcc:
    @staticmethod
    def valid_user_id(user_id, password):
        # We verify if the username is available
        user_obj = mongo_db.users.find_one({'user_id': user_id})

        if user_obj == None and password != None:
            encrypted_pw = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
            print(encrypted_pw)

            mongo_db.users.insert_one({'user_id': user_id, 'password': encrypted_pw, 'chats': [], 'contacts': []})
            return True
        return False

    @staticmethod
    def store_user(user_id):
        pass