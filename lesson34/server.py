import asyncio
import json

from datetime import datetime

all_messages = []
rec_mess = []
transport_all = []


class Server(asyncio.Protocol):
    def __init__(self):
        self.new_client = False
        self.all_messages = [{"Type": "Messages", "List_messages": rec_mess}]

    def connection_made(self, transport):
        self.peername = transport.get_extra_info('peername')
        print(f"Connection from {self.peername}")
        welcome_msg = {"Message": "Welcome to our chat!"}
        self.transport = transport
        if self.transport not in transport_all:
            if rec_mess != []:
                new_client_msg_connect = {"Message": "New Client connect!!!"}
                for clients in transport_all:
                    clients.write(json.dumps(new_client_msg_connect).encode())
                history = []
                history_dict = {}
                history_dict["Type"] = "History"
                history_dict["Welcom_message"] = welcome_msg
                history_dict["Previous_message"] = "Previous messages:"
                history_dict["List_messages"] = rec_mess
                history_dict["End_history_message"] = "_"*40
                history.append(history_dict)
                print(history)
                self.transport.write(json.dumps(history).encode())
            else:
                self.transport.write(json.dumps(welcome_msg).encode())
            transport_all.append(self.transport)
            self.new_client = True

    def data_received(self, data):
        message = data.decode()
        input_data = self.return_dict(message)
        rec_mess.append(input_data)
        send_data_list = []
        send_data_list.append(input_data)
        # if self.new_client == True:
        #     for clients in transport_all:
        #         clients.write(json.dumps())
        #     self.new_client = False
        # else:
        send_data = [{"Type": "Messages", "List_messages": send_data_list}]
        for clients in transport_all:
            clients.write(json.dumps(send_data).encode())

    def connection_lost(self, exc):
        print(f"Close the {self.peername} socket")
        transport_all.remove(self.transport)
        self.transport.close()

    def return_dict(self, message):
        split_msg = message.split(':')
        return {
            "User": f"{split_msg[0]}",
            'Message': f"{split_msg[1]}",
            "Date": f"{datetime.utcnow().strftime('%m/%d/%Y, %H:%M:%S')}"
        }



async def main():
    loop = asyncio.get_event_loop()

    server = await loop.create_server(Server, '127.0.0.1', 8886)
    async with server:
        await server.serve_forever()

    # print(f'Servering on {server.sockets[0].getsockname()}')


if __name__ == '__main__':
    asyncio.run(main())

