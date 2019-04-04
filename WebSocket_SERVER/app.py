from flask import Flask

import asyncio
import websockets

app = Flask(__name__)


# @app.route("/")
# def index():
#     return "Hello World"

@asyncio.coroutine
def hello(websocket, path):
    name = yield from websocket.recv()
    print("> {}".format(name))

    greeting = "Hello {} !".format(name)

    yield from websocket.send(greeting)
    print("< {}".format(greeting))

start_server = websockets.serve(hello, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    app.run()
