import asyncio
import random
import time
import json


class EchoClient(asyncio.Protocol):
    def __init__(self, loop, user):
        self.loop = loop
        self.user = user
        self.message = ''
        self.output_callback = None

    def set_output_callback(self, output):
        self.output_callback = output

    def connection_made(self, transport):
        self.transport = transport
        # self.send(f'{self.message}')

    def connection_lost(self, exc):
        print('The server closed the connection')
        self.loop.stop()

    def data_received(self, data):
        if data:
            print(f"{data.decode()}")
            message = data.decode()
            json_load = json.loads(message)
            if isinstance(json_load, dict):
                self.output_callback(json_load["Message"])
            if isinstance(json_load, list):
                if json_load[0]["Type"] == "History":
                    self.output_callback(json_load[0]["Welcom_message"]["Message"])
                    self.output_callback(json_load[0]["Previous_message"])
                    for item in json_load[0]["List_messages"]:
                        self.output_callback(f'({item["Date"]}){item["User"]}: {item["Message"]}')
                    self.output_callback(json_load[0]["End_history_message"])
                elif json_load[0]["Type"] == "Messages":
                    for item in json_load[0]["List_messages"]:
                        self.output_callback(f'({item["Date"]}){item["User"]}: {item["Message"]}')

    def send(self, message):
        # msg = f'{username}: {message}'
        self.transport.write(message.encode())


def main():
    loop = asyncio.get_event_loop()

    message = 'HEEEY'
    coro = loop.create_connection(lambda: EchoClient('Client_1', message, loop), '127.0.0.1', 8888)

    loop.run_until_complete(coro)
    loop.run_forever()
    loop.close()


if __name__ == '__main__':
    main()

