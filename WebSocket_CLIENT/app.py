from flask import Flask

import asyncio
import websockets

import json


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


@asyncio.coroutine
def testing_dict():
    websocket = yield from websockets.connect(
        'ws://localhost:8765/')

    try:
        je = json.dumps({'painel_id': '1', 'transmission_status_value': False})
        jef = json.loads(je)

        yield from websocket.send(je)
        print()
        print("< o JSON sent is: {}".format(je))
        print("< o painel_id sent is: {}".format(jef['painel_id']))
        print("< o transmission_status_value sent is: {}".format(jef['transmission_status_value']))
        print()

        jr = yield from websocket.recv()
        jrf = json.loads(jr)

        jro = json.dumps({'painel_id': jrf['painel_id'], 'transmission_status_value': jrf['transmission_status_value']}, sort_keys=True)

        print()
        print("> o JSON receiving is: {}".format(jr))
        print("> o painel_id receiving is: {}".format(jrf['painel_id']))
        print("> o transmission_status_value receiving is: {}".format(jrf['transmission_status_value']))
        print()

    finally:
        yield from websocket.close()


# asyncio.get_event_loop().run_until_complete(hello())
# asyncio.get_event_loop().run_until_complete(soma())
asyncio.get_event_loop().run_until_complete(testing_dict())


if __name__ == "__main__":
    app.run()
