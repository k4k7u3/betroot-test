import sys
from functools import partial
import random

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

class MyWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_of_tab = []
        self.setWindowTitle("Like a Telegram =)")
        self.setFixedSize(500, 300)
        self.widget = QWidget()
        self.main_layout = QGridLayout()
        self.main_layout.setSpacing(10)
        self.setLayout(self.main_layout)
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)
        self._menu_bar()

    def _menu_bar(self):
        self.menu_bar = QMenuBar()
        self.main_layout.addWidget(self.menu_bar, 0, 0)
        self._create_menu_bar()
        # self.space = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # self.main_layout.addItem(self.space)

    def _create_menu_bar(self):
        self.action_file = self.menu_bar.addMenu("File")
        self.new_client = self.action_file.addAction('New Client')
        self.close_client = self.action_file.addAction('Close Client')
        self.tab_widget = QTabWidget()
        self.main_layout.addWidget(self.tab_widget, 1, 0)
        self.new_client.triggered.connect(partial(self.add_tab_bar))
        self.close_client.triggered.connect(partial(self.del_tab_bar))

    def add_tab_bar(self):
        self.new_tab = QWidget()
        num_of_tab = self.tab_widget.addTab(self.new_tab, f'User {int(random.random() * 1000)}')
        self.list_of_tab.append(num_of_tab)
        self.new_tab_layout = QGridLayout()
        self.user_name = QLabel('User name: ')
        self.new_tab_layout.addWidget(self.user_name, 0, 0)
        self.new_tab.setLayout(self.new_tab_layout)
        self.input_name = QLineEdit()
        self.new_tab_layout.addWidget(self.input_name, 0, 1)
        self.button_connect = QPushButton('Connect')
        self.new_tab_layout.addWidget(self.button_connect, 0, 2)
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.new_tab_layout.addWidget(self.text_edit, 1, 0, 1, 3)
        self.button_connect.clicked.connect(partial(self.connect))
        self.msg = QLabel('Message: ')
        self.new_tab_layout.addWidget(self.msg, 2, 0)
        self.input_message = QLineEdit()
        self.new_tab_layout.addWidget(self.input_message, 2, 1)
        self.button_send = QPushButton('send')
        self.new_tab_layout.addWidget(self.button_send, 2, 2)
        self.button_send.clicked.connect(partial(self.send))
        self.space = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.new_tab_layout.addItem(self.space)

    def del_tab_bar(self):
        self.tab_widget.removeTab(self.tab_widget.currentIndex())

    def connect(self):
        self.input_user_name = self.input_name.text()

    def send(self):
        self.input_msg = self.input_message.text()
        self.text_edit.append(f'{self.input_user_name}: {self.input_msg}')
        self.input_message.setText("")


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()


