
from env_setup import set_keys

from sanic import Sanic
from sanic.response import json, text
from pymongo import MongoClient


app = Sanic()
keys = set_keys('MONGO_URL')

mongo_db = MongoClient(keys['MONGO_URL'])['intervals-dev']


@app.route('/')
async def homepage(request):
    return text("test")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

