import sys
from functools import partial
from random import random
import asyncio

from typing import Dict, List, Union, Optional, NoReturn
from PyQt5 import Qt, QtCore
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QHBoxLayout,
                             QVBoxLayout,
                             QGridLayout,
                             QFormLayout,
                             QMainWindow,
                             QPushButton,
                             QLineEdit,
                             QLabel,
                             QMenuBar,
                             QPlainTextEdit,
                             QAction,
                             QSpacerItem,
                             QSizePolicy,
                             QGroupBox,
                             QScrollArea,
                             QScrollBar,
                             QListWidgetItem,
                             QTextEdit,
                             QTabWidget)
from quamash import QEventLoop

from client import EchoClient

class MyWindow(QMainWindow):
    def __init__(self, loop, client):
        super().__init__()
        self.list_of_tab = []
        self.loop_widget = loop
        self.client = client
        self.client.set_output_callback(self.output)
        self.__init_widget()

    def output(self, message):
        self.text_edit.append(message)

    def __init_widget(self):
        self.setWindowTitle("Like a Telegram =)")
        self.setFixedSize(350, 400)
        self.widget = QWidget()
        self.main_layout = QGridLayout()
        self.main_layout.setSpacing(10)
        self.setLayout(self.main_layout)
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)
        self._menu()

    def _menu(self):
        self.user_name_label = QLabel('User name: ')
        self.main_layout.addWidget(self.user_name_label, 0, 0)
        self.input_user_name = QLineEdit()
        self.input_user_name.setText("")
        self.main_layout.addWidget(self.input_user_name, 0, 1)
        self.button_save = QPushButton('Save')
        self.main_layout.addWidget(self.button_save, 0, 2)
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setMouseTracking(True)
        self.text_edit.textSelected = False
        self.main_layout.addWidget(self.text_edit, 1, 0, 1, 3)
        self.message_label = QLabel('Message: ')
        self.main_layout.addWidget(self.message_label, 2, 0)
        self.input_message_lineedit = QLineEdit()
        self.main_layout.addWidget(self.input_message_lineedit, 2, 1)
        self.button_send = QPushButton('Send')
        self.main_layout.addWidget(self.button_send, 2, 2)
        self.button_close_connection = QPushButton('Close connection')
        self.main_layout.addWidget(self.button_close_connection, 3, 0, 3, 3)

        self.button_save.clicked.connect(partial(self.save_user_name))
        self.button_send.clicked.connect(partial(self.send_on_server))
        self.button_close_connection.clicked.connect(partial(self.close_connection))

    def save_user_name(self):
        self.user_name = self.input_user_name.text()
        if self.user_name == "":
            self.user_name = f'User{int(random()*1000)}'

    def send_on_server(self):
        self.input_message = self.input_message_lineedit.text()
        self.input_message_lineedit.setText("")
        self.client.send(f'{self.user_name}: {self.input_message}')

    def close_connection(self):
        self.client.connection_lost()


class App(QApplication):
    def __init__(self):
        QApplication.__init__(self, sys.argv)
        self.loop = QEventLoop(self)
        asyncio.set_event_loop(self.loop)

        self.client = EchoClient(self.loop, f'User {int(random() * 1000)}')
        self.loop.create_task(self.start())

        self.gui = MyWindow(self.loop, self.client)
        self.gui.show()
        self.loop.run_forever()

    async def start(self):
        clientConnection = self.loop.create_connection(lambda: self.client, '127.0.0.1', 8886)
        await asyncio.wait_for(clientConnection, 10000, loop=self.loop)


def main():
    App()


if __name__ == '__main__':
    main()


