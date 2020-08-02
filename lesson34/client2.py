import asyncio


class EchoClient(asyncio.Protocol):
    def __init__(self, message, loop):
        self.message = message
        self.loop = loop

    def connection_made(self, transport):
        transport.write(self.message.encode())

    def data_received(self, data):
        print(f"{data.decode()}")

    def connection_lost(self, exc):
        print('The server closed the connection')
        self.loop.stop()


loop = asyncio.get_event_loop()

message = 'Client_2'
coro = loop.create_connection(lambda: EchoClient(message, loop), '127.0.0.1', 8888)
loop.run_until_complete(coro)
loop.run_forever()
loop.close()

