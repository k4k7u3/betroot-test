import requests
import sys

from functools import partial
from typing import Dict, List, Union, Optional, NoReturn

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QHBoxLayout,
                             QVBoxLayout,
                             QGridLayout,
                             QFormLayout,
                             QMainWindow,
                             QPushButton,
                             QLineEdit,
                             QLabel)


class MyWindow(QMainWindow):
    def __init__(self, *args, **kwargs) -> NoReturn:
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Custom Weather")
        self.setFixedSize(250, 250)
        self.widget = QWidget()
        self.main_layout = QVBoxLayout()
        self._input_city()
        self._add_button()
        self._add_msg()
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)

    def _input_city(self) -> NoReturn:
        self.form_layout = QFormLayout()
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.form_layout.addRow("City: ", self.display)
        self.main_layout.addLayout(self.form_layout)

    def _add_button(self) -> NoReturn:
        self.button_layout = QVBoxLayout()
        btn = QPushButton("Find out the weather")
        btn.clicked.connect(self.weather)
        self.button_layout.addWidget(btn)
        self.main_layout.addLayout(self.button_layout)

    def _add_msg(self) -> NoReturn:
        self.msg = QLabel("")
        self.msg1 = QLabel("")
        self.msg2 = QLabel("")
        self.msg3 = QLabel("")
        self.msg4 = QLabel("")
        self.msg5 = QLabel("")
        self.msg6 = QLabel("")
        self.main_layout.addWidget(self.msg)
        self.main_layout.addWidget(self.msg1)
        self.main_layout.addWidget(self.msg2)
        self.main_layout.addWidget(self.msg3)
        self.main_layout.addWidget(self.msg4)
        self.main_layout.addWidget(self.msg5)
        self.main_layout.addWidget(self.msg6)

    def weather(self) -> NoReturn:
        value: str = self.display.text()
        if value == "":
            self.msg.setText("You must input name of city")
            self.msg1.setText("")
            self.msg2.setText("")
            self.msg3.setText("")
            self.msg4.setText("")
            self.msg5.setText("")
            self.msg6.setText("")
            return
        if self.msg.text():
            self.msg.setText("")
        resp = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather",
            params={"q": value, "units": "metric", "lang": "ru", "appid": "e202fd651779d31cb4bc74b0e0550e9d"})
        data: Dict = resp.json()
        if int(data["cod"]) >= 400:
            self.msg.setText(data["message"])
            self.msg1.setText("")
            self.msg2.setText("")
            self.msg3.setText("")
            self.msg4.setText("")
            self.msg5.setText("")
            self.msg6.setText("")
            return
        a = u'\u2103'
        temperature: Union[int, float] = data["main"]["temp"]
        self.msg.setText(f"Temperature: {temperature} {a}")
        self.msg1.setText(f"Feels like: {data['main']['feels_like']} {a}")
        self.msg2.setText(f"Main: {data['weather'][0]['main']}")
        self.msg3.setText(f"Description: {data['weather'][0]['description']}")
        self.msg4.setText(f"Max Temp.: {data['main']['temp_max']} {a}")
        self.msg5.setText(f"Min Temp.: {data['main']['temp_min']} {a}")
        self.msg6.setText(f"Humidity: {data['main']['humidity']} %")


def main() -> NoReturn:
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
