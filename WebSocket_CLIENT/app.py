from flask import Flask

import asyncio
import websockets


app = Flask(__name__)


# @app.route("/")
# def index():
#     return "Hello World"

@asyncio.coroutine
def hello():
    websocket = yield from websockets.connect(
        'ws://localhost:8765/')

    try:
        name1 = input("What's your name? ")

        yield from websocket.send(name1)
        print("< {}".format(name1))

        greeting = yield from websocket.recv()
        print("> {}".format(greeting))

    finally:
        yield from websocket.close()

asyncio.get_event_loop().run_until_complete(hello())


if __name__ == "__main__":
    app.run()
