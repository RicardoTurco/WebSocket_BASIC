from flask import Flask

import asyncio
import websockets

import json


app = Flask(__name__)


@asyncio.coroutine
def hello(websocket, path):
    name = yield from websocket.recv()
    print("> {}".format(name))

    greeting = "Hello {} !".format(name)

    yield from websocket.send(greeting)
    print("< {}".format(greeting))


@asyncio.coroutine
def soma(websocket, path):
    nr = yield from websocket.recv()

    nrf = list(nr.split(","))

    print()
    print("> the first number received was: {}".format(nrf[0]))
    print("> the second number received was: {}".format(nrf[1]))
    print()

    c = (int(nrf[0]) + int(nrf[1]))
    d = str(c)

    yield from websocket.send(d)
    print("< the result sent was: {}".format(d))


# start_server = websockets.serve(hello, 'localhost', 8765)
start_server = websockets.serve(soma, 'localhost', 8765)


asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    app.run()
