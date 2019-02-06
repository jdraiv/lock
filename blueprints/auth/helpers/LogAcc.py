
import bcrypt
from main import mongo_db


class LogAcc:
    @staticmethod
    def generate_tokens(user_id):
        pass

    @staticmethod
    def valid_credentials(user_id, password):
        user_obj = mongo_db.users.find_one({'user_id': user_id})

        if user_obj != None:
            return bcrypt.checkpw(str.encode(password), user_obj['password'])
        return False