import asyncio

rec_mess = {}
transport_all = []


class Server(asyncio.Protocol):
    def connection_made(self, transport):
        self.peername = transport.get_extra_info('peername')
        print(f"Connection from {self.peername}")
        self.transport = transport
        transport_all.append(self.transport)

    def data_received(self, data):
        message = data.decode()
        # print(f"Data recieve {message}")
        rec_mess[f'{self.peername[1]}'] = message
        print(f"Send: {rec_mess}")
        # print(transport_all)
        for i in transport_all:
            # print(i.__dict__['_sock'])
            for key, val in rec_mess.items():
                i.write(bytes(f'{key}: {val} ', encoding="utf-8"))

    def connection_lost(self, exc):
        print(f"Close the {self.peername} socket")
        self.transport.close()


async def main():
    loop = asyncio.get_event_loop()

    server = await loop.create_server(Server, '127.0.0.1', 8888)
    async with server:
        await server.serve_forever()

    # print(f'Servering on {server.sockets[0].getsockname()}')

asyncio.run(main())

