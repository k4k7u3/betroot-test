import asyncio

rec_mess = {}
transport_all = []

class Server(asyncio.Protocol):
    def __init__(self):
        self.new_client = False

    def connection_made(self, transport):
        self.peername = transport.get_extra_info('peername')
        print(f"Connection from {self.peername}")
        self.transport = transport
        if self.transport not in transport_all:
            self.new_client = True

    def data_received(self, data):
        message = data.decode()
        # print(f"Data recieve {message}")
        rec_mess[f'{self.peername[1]}'] = message
        print(f"Send: {rec_mess}")
        if self.new_client == True:
            for key, val in rec_mess.items():
                self.transport.write(bytes(f'{key}: {val} ', encoding="utf-8"))
            for i in transport_all:
                i.write(bytes(f'{self.peername[1]}: {message}', encoding="utf-8"))
            transport_all.append(self.transport)
        else:
            for i in transport_all:
                i.write(bytes(f'{self.peername[1]}: {message}', encoding="utf-8"))

    def connection_lost(self, exc):
        print(f"Close the {self.peername} socket")
        transport_all.remove(self.transport)
        self.transport.close()
        # удалять клиента


async def main():
    loop = asyncio.get_event_loop()

    server = await loop.create_server(Server, '127.0.0.1', 8888)
    async with server:
        await server.serve_forever()

    # print(f'Servering on {server.sockets[0].getsockname()}')


if __name__ == '__main__':
    asyncio.run(main())

