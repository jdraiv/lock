

from sanic import Sanic
from sanic.response import json, text


app = Sanic()


@app.route('/')
async def homepage(request):
    return text("test")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

