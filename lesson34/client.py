import asyncio
import random
import time


class EchoClient(asyncio.Protocol):
    def __init__(self, user, message, loop):
        self.message = message
        self.loop = loop
        self.user = user

    def connection_made(self, transport):
        self.transport = transport
        self.send(f'{self.message}')

    def connection_lost(self, exc):
        print('The server closed the connection')
        self.loop.stop()

    def data_received(self, data):
        print(f"{data.decode()}")
        # self.send(str(random.random()))

    def send(self, data):
        self.transport.write(data.encode())


loop = asyncio.get_event_loop()

message = 'HEEEY'
coro = loop.create_connection(lambda: EchoClient('Client_1', message, loop), '127.0.0.1', 8888)

loop.run_until_complete(coro)
loop.run_forever()
loop.close()

