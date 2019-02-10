
import bcrypt
from main import mongo_db
from global_helpers.response import internal_response


class LogAcc:
    @staticmethod
    def generate_tokens(user_id):
        pass

    @staticmethod
    def valid_credentials(user_id, password):
        user_obj = mongo_db.users.find_one({'user_id': user_id})

        if user_obj != None:
            if bcrypt.checkpw(str.encode(password), user_obj['password']):
                return internal_response(status="success", message="User authenticated")
        return internal_response(status="error", message="Incorrect username or password")
