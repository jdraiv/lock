
from env_setup import set_keys

from sanic import Sanic
from sanic.response import json, text
from sanic.websocket import WebSocketProtocol
from pymongo import MongoClient


app = Sanic()
keys = set_keys('MONGO_URL', 'BCRYPT_KEY', 'JWT_KEY', 'RTK_KEY')
mongo_db = MongoClient(keys['MONGO_URL'])['lock-dev']


from blueprints.auth.main import auth_module
from blueprints.contacts.main import contacts_module

from decorators.auth_decorators import jwt_required


app.blueprint(auth_module)
app.blueprint(contacts_module)


@app.route('/')
async def homepage(request):
    return text("test")


@app.route('/protected')
@jwt_required()
async def test(request):
    return text("Protected route")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, protocol=WebSocketProtocol)

