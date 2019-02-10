
from sanic import Blueprint


chats_module = Blueprint('chats_module')


@chats_module.websocket('/chat_test')
async def feed(request, ws):
    while True:
        await ws.send("hello")
        data = await ws.recv()
        print('Received: ' + data)