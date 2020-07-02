import sys

from functools import partial
from typing import Dict, List, Union, Optional, NoReturn
from math import sqrt

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QHBoxLayout,
                             QVBoxLayout,
                             QGridLayout,
                             QMainWindow,
                             QPushButton,
                             QLineEdit,
                             QLabel)


class MyWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.firstvalue: Union[int, float] = 0
        self.operation: str = ""
        self.secOper: str = ""
        self.secondvalue: Union[int, float] = 0
        self.resultOperation: Union[int, float] = 0
        self.value1 = ""
        self.fail: str = "На ноль делить нельзя"
        self.fail1: str = "Введены неверные данные"
        self.setWindowTitle("Calculator v.0.1")
        self.setFixedSize(300, 300)
        self.widget = QWidget()
        self.mainLayout = QVBoxLayout()
        self._createdDisplay()
        self._createdButtons()
        self.widget.setLayout(self.mainLayout)
        self.setCentralWidget(self.widget)
        self.processclick()

    def _createdDisplay(self) -> NoReturn:
        self.display = QLineEdit("0")
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.mainLayout.addWidget(self.display)

    def _createdButtons(self) -> NoReturn:
        buttonLayout = QGridLayout()
        buttons: List[Dict] = [
            {
                "name": '%',
                "row": 0,
                "col": 0,
            },
            {
                "name": 'CE',
                "row": 0,
                "col": 1,
            },
            {
                "name": 'C',
                "row": 0,
                "col": 2,
            },
            {
                "name": '<-',
                "row": 0,
                "col": 3,
            },
            {
                "name": '1/x',
                "row": 1,
                "col": 0,
            },
            {
                "name": 'x^2',
                "row": 1,
                "col": 1,
            },
            {
                "name": 'sqrt(x)',
                "row": 1,
                "col": 2,
            },
            {
                "name": '/',
                "row": 1,
                "col": 3,
            },
            {
                "name": '7',
                "row": 2,
                "col": 0,
            },
            {
                "name": '8',
                "row": 2,
                "col": 1,
            },
            {
                "name": '9',
                "row": 2,
                "col": 2,
            },
            {
                "name": '*',
                "row": 2,
                "col": 3,
            },
            {
                "name": '4',
                "row": 3,
                "col": 0,
            },
            {
                "name": '5',
                "row": 3,
                "col": 1,
            },
            {
                "name": '6',
                "row": 3,
                "col": 2,
            },
            {
                "name": '-',
                "row": 3,
                "col": 3,
            },
            {
                "name": '1',
                "row": 4,
                "col": 0,
            },
            {
                "name": '2',
                "row": 4,
                "col": 1,
            },
            {
                "name": '3',
                "row": 4,
                "col": 2,
            },
            {
                "name": '+',
                "row": 4,
                "col": 3,
            },
            {
                "name": '+/-',
                "row": 5,
                "col": 0,
            },
            {
                "name": '0',
                "row": 5,
                "col": 1,
            },
            {
                "name": '.',
                "row": 5,
                "col": 2,
            },
            {
                "name": '=',
                "row": 5,
                "col": 3,
            }
        ]
        self.buttons: Dict = {}
        for buttonConfig in buttons:
            name = buttonConfig.get("name")
            btn = QPushButton(name)
            self.buttons[name] = btn
            buttonLayout.addWidget(btn,
                                   buttonConfig["row"],
                                   buttonConfig["col"])
        self.mainLayout.addLayout(buttonLayout)

    def processclick(self) -> NoReturn:
        for buttonName in self.buttons:
            btn = self.buttons[buttonName]
            if (buttonName == "0" or buttonName == "1" or buttonName == "2" or buttonName == "3"
                or buttonName == "4" or buttonName == "5" or buttonName == "6"
                or buttonName == "7" or buttonName == "8" or buttonName == "9"):
                btn.clicked.connect(partial(self._printvalue, buttonName))
            elif buttonName == "<-":
                btn.clicked.connect(self._deletebystep)
            elif buttonName == "C":
                btn.clicked.connect(self._clearall)
            elif buttonName == "CE":
                btn.clicked.connect(self._clearlast)
            elif buttonName == ".":
                btn.clicked.connect(self._printpoint)
            elif buttonName == "+":
                btn.clicked.connect(self._operationAdd)
            elif buttonName == "-":
                btn.clicked.connect(self._operationMinus)
            elif buttonName == "*":
                btn.clicked.connect(self._operationMulti)
            elif buttonName == "/":
                btn.clicked.connect(self._operationDiv)
            elif buttonName == "=":
                btn.clicked.connect(self._equally)
            elif buttonName == "+/-":
                btn.clicked.connect(self._plusMinusChange)
            elif buttonName == '1/x':
                btn.clicked.connect(self._oneDivX)
            elif buttonName == 'x^2':
                btn.clicked.connect(self._squared)
            elif buttonName == 'sqrt(x)':
                btn.clicked.connect(self._sqrt)
            elif buttonName == '%':
                btn.clicked.connect(self._buttonPercent)



    # функция для определения числа (инт или флоат)
    def _numbersTypeDetermenition(self, tempvalue: List) -> NoReturn:
        if "." in tempvalue[0]:
            self.firstvalue = float(tempvalue[0])
        else:
            self.firstvalue = int(tempvalue[0])
        if "." in tempvalue[1]:
            self.secondvalue = float(tempvalue[1])
        else:
            self.secondvalue = int(tempvalue[1])

    def _firstNumberTypeDetermenition(self, tempvalue: List) -> NoReturn:
        if "." in tempvalue[0]:
            self.firstvalue = float(tempvalue[0])
        else:
            self.firstvalue = int(tempvalue[0])

    def _secondNumberTypeDetermenition(self, tempvalue: List) -> NoReturn:
        if "." in tempvalue[1]:
            self.secondvalue = float(tempvalue[1])
        else:
            self.secondvalue = int(tempvalue[1])

    # функция для обработки введенного на экране
    def _fieldprocessing(self):
        value = self.display.text()
        if self.operation == "":
            return
        else:
            if int(self.firstvalue) < 0:
                self.tempFirstvalue = self.firstvalue
                self.value1 = value[1:]
                tempvalue = self.value1.split(self.operation)
            else:
                tempvalue = value.split(self.operation)
            if tempvalue[1] == "":
                return
            else:
                if self.value1 != "":
                    self.firstvalue = self.tempFirstvalue
                    tempvalue[0] = str(self.firstvalue)
                if self.operation == "+":
                    self._numbersTypeDetermenition(tempvalue)
                    self.firstvalue += self.secondvalue
                    self.operation = ""
                    self.display.setText(str(self.firstvalue))
                elif self.operation == "-":
                    self._numbersTypeDetermenition(tempvalue)
                    self.firstvalue -= self.secondvalue
                    self.operation = ""
                    self.display.setText(str(self.firstvalue))
                elif self.operation == "*":
                    self._numbersTypeDetermenition(tempvalue)
                    self.firstvalue *= self.secondvalue
                    self.operation = ""
                    self.display.setText(str(self.firstvalue))
                elif self.operation == "/":
                    self._numbersTypeDetermenition(tempvalue)
                    if self.secondvalue != 0:
                        self.firstvalue /= self.secondvalue
                        self.operation = ""
                        self.display.setText(str(self.firstvalue))
                    else:
                        self.display.setText(self.fail)
                        self.operation = "Error"


    # функция для обработки кнопки "="
    def _equally(self):
        value = self.display.text()
        if self.operation == "":
            return
        else:
            if value.count("-") == 2:
                if self.operation != "-":
                    tempvalue = value.split(self.operation)
                else:    
                    positionSymbol = value.rfind("-")                                                       # Часть когда, где если у нас выражение "-12-12"
                    tempvalue = [value[:positionSymbol], value[positionSymbol:]]                            # и я жму на "=", что бы не возникало ошибки
                    self.operation = "+"                                                                    #
            else:
                tempvalue = value.split(self.operation)
                self.secOper = "="
            if self.operation == "+":
                if tempvalue[1] == "":
                    self._firstNumberTypeDetermenition(tempvalue)
                    self.operation = ""
                    self.secondvalue = 0
                    self.display.setText(tempvalue[0])
                else:
                    self._numbersTypeDetermenition(tempvalue)
                    self.firstvalue += self.secondvalue
                    self.operation = ""
                    self.secondvalue = 0
                    self.display.setText(str(self.firstvalue))
            elif self.operation == "-":
                if tempvalue[1] == "":
                    self._firstNumberTypeDetermenition(tempvalue)
                    self.operation = ""
                    self.secondvalue = 0
                    self.display.setText(tempvalue[0])
                else:
                    self._numbersTypeDetermenition(tempvalue)
                    self.firstvalue -= self.secondvalue
                    self.operation = ""
                    self.secondvalue = 0
                    self.display.setText(str(self.firstvalue))
            elif self.operation == "*":
                if tempvalue[1] == "":
                    self._firstNumberTypeDetermenition(tempvalue)
                    self.operation = ""
                    self.secondvalue = 0
                    self.display.setText(tempvalue[0])
                else:
                    self._numbersTypeDetermenition(tempvalue)
                    self.firstvalue *= self.secondvalue
                    self.operation = ""
                    self.secondvalue = 0
                    self.display.setText(str(self.firstvalue))
            elif self.operation == "/":
                if tempvalue[1] == "":
                    self._firstNumberTypeDetermenition(tempvalue)
                    self.operation = ""
                    self.secondvalue = 0
                    self.display.setText(tempvalue[0])
                else:
                    self._numbersTypeDetermenition(tempvalue)
                    if self.secondvalue != 0:
                        self.firstvalue /= self.secondvalue
                        self.operation = ""
                        self.secondvalue = 0
                        self.display.setText(str(self.firstvalue))
                    else:
                        self.display.setText(self.fail)
                        self.operation = "Error"

    # функция для изменения знака числа
    def _plusMinusChange(self) -> NoReturn:
        if self.operation == "Error":
            return
        elif self.operation == "":
            value = self.display.text()
            tempvalue = value.split(" ")
            self._firstNumberTypeDetermenition(tempvalue)
            self.firstvalue *= -1
            self.display.setText(str(self.firstvalue))
        else:
            value = self.display.text()
            if value.count("-") == 1:
                if self.operation == "+":
                    tempvalue = value.split(self.operation)
                    if tempvalue[1] == "":                                                                   # проверка, если у нас есть число "-12+" и я нажму
                        return                                                                               # "+/-" что бы не крашнулась прога
                    self._numbersTypeDetermenition(tempvalue)
                    self.operation = "-"
                    self.display.setText(str(self.firstvalue) + self.operation + str(self.secondvalue))
                elif self.operation != "+" and self.operation != "-":
                    tempvalue = value.split(self.operation)
                    if tempvalue[1] == "":
                        return
                    self._numbersTypeDetermenition(tempvalue)
                    self.secondvalue *= -1
                    self.display.setText(str(self.firstvalue) + self.operation + str(self.secondvalue))
                else:
                    positionSymbol = value.rfind("-")
                    tempvalue = [value[:positionSymbol], value[positionSymbol:]]
                    self._numbersTypeDetermenition(tempvalue)
                    if self.secondvalue < 0:
                        self.operation = "+"
                        self.secondvalue *= -1
                        self.display.setText(str(self.firstvalue) + self.operation + str(self.secondvalue))
            elif value.count("-") == 2:
                if self.operation != "-":                                                                           #-----------------------------------------
                    tempvalue = value.split(self.operation)                                                         # Эта проверка для того, что бы если у нас
                    self._numbersTypeDetermenition(tempvalue)                                                       # есть -12*3 и мы жмакаем на кнопку "+/-"
                    self.secondvalue *= -1                                                                          # у нас не крашилась программа
                    self.display.setText(str(self.firstvalue) + self.operation + str(self.secondvalue))             #-----------------------------------------
                else:
                    positionSymbol = value.rfind("-")
                    tempvalue = [value[:positionSymbol], value[positionSymbol:]]
                    self._numbersTypeDetermenition(tempvalue)
                    if self.secondvalue < 0:
                        self.operation = "+"
                        self.secondvalue *= -1
                        self.display.setText(str(self.firstvalue) + self.operation + str(self.secondvalue))
            else:
                tempvalue = value.split(self.operation)
                if tempvalue[1] == "":
                    return
                else:
                    if self.operation == "+":
                        self.operation = "-"
                        self._numbersTypeDetermenition(tempvalue)
                        self.display.setText(str(self.firstvalue) + self.operation + str(self.secondvalue))
                    else:
                        self._numbersTypeDetermenition(tempvalue)
                        self.secondvalue *= -1
                        self.display.setText(str(self.firstvalue) + self.operation + str(self.secondvalue))

    # функция для обработки кнопки "+"
    def _operationAdd(self) -> NoReturn:
        self._fieldprocessing()
        if self.operation == "":
            value = self.display.text()
            if value == self.fail or value == self.fail1:                           # проверка, для того, что бы если у нас на экране self.fail и мы
                value = "0"                                                         # нажимаем операцию какую либо, то что-бы начиналось с 0
            if "." in value:
                self.firstvalue = float(value)
            else:
                self.firstvalue = int(value)
            self.display.setText(value + "+")
            self.operation = "+"
        elif self.operation == "+":
            value = self.display.text()
            tempvalue = value.split("+")
            if tempvalue[1] == "":                                                  #--------------------------
                self.operation = "+"                                                # Этот кусок кода, для того, что бы если у нас есть
                self.display.setText(value)                                         # 12+ и при повторном нажатии на + не крашилась программа
                return                                                              #--------------------------
            if "." in tempvalue[1]:
                self.secondvalue = float(tempvalue[1])
            else:
                self.secondvalue = int(tempvalue[1])
            self.firstvalue = self.firstvalue + self.secondvalue
            self.secondvalue = 0
            self.display.setText(str(self.firstvalue) + "+")
        elif self.operation == "Error":
            value = self.display.text()
            self.operation = ""
            self.display.setText(value)
        elif self.operation != "" and self.operation != "+":
            value = self.display.text()
            # if self.operation == "/":
            #     self.operation = "+"
            #     self.display.setText(value)
            # else:
            self.operation = "+"
            self.display.setText(value[:-1] + "+")

    # функция для обработки кнопки "-"
    def _operationMinus(self) -> NoReturn:
        self._fieldprocessing()
        if self.operation == "":
            value = self.display.text()
            if value == self.fail or value == self.fail1:                           # проверка, для того, что бы если у нас на экране self.fail и мы
                value = "0"                                                         # нажимаем операцию какую либо, то что-бы начиналось с 0
            if "." in value:
                self.firstvalue = float(value)
            else:
                self.firstvalue = int(value)
            self.display.setText(value + "-")
            self.operation = "-"
        elif self.operation == "-":
            value = self.display.text()
            if value.count("-") == 2:
                positionSymbol = value.rfind("-")
                tempvalue = [value[:positionSymbol], value[positionSymbol:]]
                if tempvalue[1] == "-":                                             # --------------------------
                    self.operation = "-"                                            # Этот кусок кода, для того, что бы если у нас есть
                    self.display.setText(value)                                     # 12+ и при повторном нажатии на + не крашилась программа
                    return                                                          # --------------------------
                self._numbersTypeDetermenition(tempvalue)
            else:
                tempvalue = value.split("-")
                if tempvalue[1] == "":                                              # --------------------------
                    self.operation = "-"                                            # Этот кусок кода, для того, что бы если у нас есть
                    self.display.setText(value)                                     # 12+ и при повторном нажатии на + не крашилась программа
                    return                                                          # --------------------------
                if "." in tempvalue[1]:
                    self.secondvalue = float(tempvalue[1])
                else:
                    self.secondvalue = int(tempvalue[1])
            self.firstvalue -= self.secondvalue
            self.secondvalue = 0
            self.display.setText(str(self.firstvalue) + "-")
        elif self.operation == "Error":
            value = self.display.text()
            self.operation = ""
            self.display.setText(value)
        elif self.operation != "" and self.operation != "-":
            value = self.display.text()
            # if self.operation == "/":
            #     self.operation = "-"
            #     self.display.setText(value)
            # else:
            self.operation = "-"
            self.display.setText(value[:-1] + "-")

    # функция для обработки кнопки "*"
    def _operationMulti(self) -> NoReturn:
        self._fieldprocessing()
        if self.operation == "":
            value = self.display.text()
            if value == self.fail or value == self.fail1:                           # проверка, для того, что бы если у нас на экране self.fail и мы
                value = "0"                                                         # нажимаем операцию какую либо, то что-бы начиналось с 0
            if "." in value:
                self.firstvalue = float(value)
            else:
                self.firstvalue = int(value)
            self.display.setText(value + "*")
            self.operation = "*"
        elif self.operation == "*":
            value = self.display.text()
            tempvalue = value.split("*")
            if tempvalue[1] == "":                                                  # --------------------------
                self.operation = "*"                                                # Этот кусок кода, для того, что бы если у нас есть
                self.display.setText(value)                                         # 12+ и при повторном нажатии на + не крашилась программа
                return                                                              # --------------------------
            if "." in tempvalue[1]:
                self.secondvalue = float(tempvalue[1])
            else:
                self.secondvalue = int(tempvalue[1])
            self.firstvalue *= self.secondvalue
            self.secondvalue = 0
            self.display.setText(str(self.firstvalue) + "*")
        elif self.operation == "Error":
            value = self.display.text()
            self.operation = ""
            self.display.setText(value)
        elif self.operation != "" and self.operation != "*":
            value = self.display.text()
            # if self.operation == "/":
            #     self.operation = "*"
            #     self.display.setText(value)
            # else:
            self.operation = "*"
            self.display.setText(value[:-1] + "*")

    # функция для обработки кнопки "/"
    def _operationDiv(self) -> NoReturn:
        self._fieldprocessing()
        if self.operation == "":
            value = self.display.text()
            if value == self.fail or value == self.fail1:                           # проверка, для того, что бы если у нас на экране self.fail и мы
                value = "0"                                                         # нажимаем операцию какую либо, то что-бы начиналось с 0
            if "." in value:
                self.firstvalue = float(value)
            else:
                self.firstvalue = int(value)
            self.display.setText(value + "/")
            self.operation = "/"
        elif self.operation == "/":
            value = self.display.text()
            tempvalue = value.split("/")
            if tempvalue[1] == "":                                                  # --------------------------
                self.operation = "/"                                                # Этот кусок кода, для того, что бы если у нас есть
                self.display.setText(value)                                         # 12+ и при повторном нажатии на + не крашилась программа
                return                                                              # --------------------------
            if tempvalue[1] == "0":
                self.firstvalue = 0
                self.operation = ""
                self.secondvalue = 0
                self.display.setText(self.fail)
                return
            if "." in tempvalue[1]:
                self.secondvalue = float(tempvalue[1])
            else:
                self.secondvalue = int(tempvalue[1])
            self.firstvalue /= self.secondvalue
            self.secondvalue = 0
            self.display.setText(str(self.firstvalue) + "/")
        elif self.operation == "Error":
            value = self.display.text()
            self.operation = ""
            self.display.setText(value)
        elif self.operation != "" and self.operation != "/":
            value = self.display.text()
            self.operation = "/"
            self.display.setText(value[:-1] + "/")

    # функция кнопки 1/x
    def _oneDivX(self) -> NoReturn:
        value = self.display.text()
        if self.operation == "":
            if value == self.fail or value == self.fail1:                           # проверка, для того, что бы если у нас на экране self.fail и мы
                value = "0"                                                         # нажимаем операцию какую либо, то что-бы начиналось с 0
            if "." in value:
                self.firstvalue = float(value)
            else:
                self.firstvalue = int(value)
            if self.firstvalue == 0:
                self.firstvalue = 0
                self.operation = ""
                self.secondvalue = 0
                self.display.setText(self.fail)
                return
            self.firstvalue = 1 / self.firstvalue
            self.display.setText(str(self.firstvalue))
        elif self.operation == "Error":
            value = self.display.text()
            self.operation = ""
            self.display.setText(value)
        else:
            tempvalue = value.split(self.operation)
            if tempvalue[1] == "":
                return
            if tempvalue[1] == "0":
                self.firstvalue = 0
                self.operation = ""
                self.secondvalue = 0
                self.display.setText(self.fail)
                return
            if self.operation == "-":
                if value.count("-") == 2:
                    positionSymbol = value.rfind("-")
                    tempvalue = [value[:positionSymbol], value[positionSymbol+1:]]
            self._numbersTypeDetermenition(tempvalue)
            self.secondvalue = 1 / self.secondvalue
            self.display.setText(str(self.firstvalue) + self.operation + str(self.secondvalue))

    # функция кнопки x^2
    def _squared(self) -> None:
        value = self.display.text()
        if self.operation == "":
            if value == self.fail or value == self.fail1:  # проверка, для того, что бы если у нас на экране self.fail и мы
                value = "0"  # нажимаем операцию какую либо, то что-бы начиналось с 0
            if "." in value:
                self.firstvalue = float(value)
            else:
                self.firstvalue = int(value)
            self.firstvalue *= self.firstvalue
            self.display.setText(str(self.firstvalue))
        elif self.operation == "Error":
            value = self.display.text()
            self.operation = ""
            self.display.setText(value)
        else:
            tempvalue = value.split(self.operation)
            if tempvalue[1] == "":
                return
            if self.operation == "-":
                if value.count("-") == 2:
                    positionSymbol = value.rfind("-")
                    tempvalue = [value[:positionSymbol], value[positionSymbol + 1:]]
            self._numbersTypeDetermenition(tempvalue)
            self.secondvalue *= self.secondvalue
            self.display.setText(str(self.firstvalue) + self.operation + str(self.secondvalue))

    # функция кнопки sqrt
    def _sqrt(self):
        value = self.display.text()
        if self.operation == "":
            if value == self.fail or value == self.fail1:                               # проверка, для того, что бы если у нас на экране self.fail и мы
                value = "0"                                                             # нажимаем операцию какую либо, то что-бы начиналось с 0
            if "." in value:
                self.firstvalue = float(value)
            else:
                self.firstvalue = int(value)
            if self.firstvalue < 0:
                self.firstvalue = 0
                self.operation = ""
                self.secondvalue = 0
                self.display.setText(self.fail1)
                return
            self.firstvalue = sqrt(self.firstvalue)
            self.display.setText(str(self.firstvalue))
        elif self.operation == "Error":
            value = self.display.text()
            self.operation = ""
            self.display.setText(value)
        else:
            tempvalue = value.split(self.operation)
            if tempvalue[1] == "":
                return
            if self.operation == "-":
                if value.count("-") == 2:
                    positionSymbol = value.rfind("-")
                    tempvalue = [value[:positionSymbol], value[positionSymbol + 1:]]
            self._numbersTypeDetermenition(tempvalue)
            if self.secondvalue < 0:
                self.firstvalue = 0
                self.operation = ""
                self.secondvalue = 0
                self.display.setText(self.fail1)
                return
            self.secondvalue = sqrt(self.secondvalue)
            self.display.setText(str(self.firstvalue) + self.operation + str(self.secondvalue))

    # функция кнопки %
    def _buttonPercent(self) -> NoReturn:
        if self.operation == "":
            self.firstvalue = "0"
            self.display.setText("0")
        elif self.operation == "Error":
            value = self.display.text()
            self.operation = ""
            self.display.setText(value)
        else:
            value = self.display.text()
            if self.operation == "-":
                if value.count("-") == 2:
                    positionSymbol = value.rfind("-")
                    tempvalue = [value[:positionSymbol], value[positionSymbol+1:]]
                else:
                    tempvalue = value.split(self.operation)
            else:
                tempvalue = value.split(self.operation)
            self._numbersTypeDetermenition(tempvalue)
            self.secondvalue = (self.firstvalue * self.secondvalue) / 100
            self.display.setText(str(self.firstvalue) + self.operation + str(self.secondvalue))



    # функция для печати чисел (0 - 9)
    def _printvalue(self, text: str) -> NoReturn:
        value = self.display.text()
        if self.operation != "":                                                    # Проверка для того, что бы если у нас есть
            if value[-1] == "0" and value[-2].isdigit != True:                      # "28/03" то 0 удаляется (чисто для красоты)
                self.display.setText(value[:-1] + text)                             # как в калькуляторе на винде
                return
        if value == "0":
            self.display.setText("")
        if value == self.fail or value == self.fail1:
            self.display.setText("")
            self.operation = ""
        if self.secOper == "=":
            if self.operation != "":
                self.display.setText(self.display.text() + text)
            else:
                self.display.setText(text)
                self.secOper = ""
        else:
            self.display.setText(self.display.text() + text)

    # функция для обработки кнопки "<-"
    def _deletebystep(self) -> None:
        value = self.display.text()
        value = value[:-1]
        if len(value) == 0:
            self.operation = ""
            self.display.setText("0")
        else:
            if self.operation != "":
                self.operation = ""
            self.display.setText(value)

    # функция для обработки кнопки "C"
    def _clearall(self) -> NoReturn:
        self.firstvalue = 0
        self.operation = ""
        self.secondvalue = 0
        self.display.setText("0")

    # функция для обработки кнопки "CE"
    def _clearlast(self) -> NoReturn:
        value = self.display.text()
        if self.operation == "":
            self.firstvalue = 0
            self.operation = ""
            self.secondvalue = 0
            self.display.setText("0")
        else:
            tempvalue = value.split(self.operation)
            self.display.setText(tempvalue[0] + self.operation)

    # функция для печати точки
    def _printpoint(self):
        value = self.display.text()
        if self.operation == "":
            if "." in value:
                pass
            else:
                self.display.setText(self.display.text() + ".")
        else:
            listvalue = value.split(self.operation)
            if "." in listvalue[1]:
                pass
            else:
                self.display.setText(self.display.text() + ".")


def main() -> NoReturn:
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

