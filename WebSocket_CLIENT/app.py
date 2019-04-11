from flask import Flask

import asyncio
import websockets


app = Flask(__name__)


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


@asyncio.coroutine
def soma():
    websocket = yield from websockets.connect(
        'ws://localhost:8765/')

    try:
        ne = "2,3"
        nef = list(ne.split(","))

        yield from websocket.send(ne)
        print()
        print("< the first number sent is: {}".format(nef[0]))
        print("< the second number sent is: {}".format(nef[1]))
        print()

        nr = yield from websocket.recv()
        print()
        print("> the result received is: {}".format(str(nr)))
        print()

    finally:
        yield from websocket.close()
        a = ''


# asyncio.get_event_loop().run_until_complete(hello())
asyncio.get_event_loop().run_until_complete(soma())


if __name__ == "__main__":
    app.run()
