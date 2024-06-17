from functools import partial

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QLineEdit, QWidget, QGridLayout, QPushButton


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setFixedSize(235,235)
        #layout
        self.genericWidget = QWidget()
        self.mainLayout = QVBoxLayout(self.genericWidget)
        self.setCentralWidget(self.genericWidget)
        #visuals
        self._createDisplay()
        self._createButtons()
        self._connButtons()

    def _createDisplay(self):
        self._input = QLineEdit()
        self._input.setFixedHeight(35)
        self._input.setAlignment(Qt.AlignRight)
        self._input.setReadOnly(True)
        self.mainLayout.addWidget(self._input)

    def _createButtons(self):
        self.calcButtons = {}
        self.layoutButtons = QGridLayout()
        #text-position
        self.calcButtons={
            '7':(0,0),
            '8': (0, 1),
            '9': (0, 2),
            '/': (0, 3),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '*': (1, 3),
            '1': (2, 0),
            '2': (2, 1),
            '3': (2, 2),
            '-': (2, 3),
            '0': (3, 0),
            '.': (3, 1),
            'C': (3, 2),
            '+': (3, 3),
            '=': (3, 4),
        }

        #add buttons to dict
        for text,pos in self.calcButtons.items():
            self.calcButtons[text] = QPushButton(text)
            self.calcButtons[text].setFixedSize(40,40)
            self.layoutButtons.addWidget(self.calcButtons[text],pos[0],pos[1])

    def _connButtons(self):
        def _expresion(text):
            self._input.setText(self._input.text() + text)
        def _c():
            self._input.clear()
        def _result():
            try:
                self._input.setText(str(eval(self._input.text()))) #wow magic
            except Exception as e:
                self._input.setText("ERROR")

        for text,button in self.calcButtons.items():
            if text == 'C':
                button.clicked.connect(_c)
            elif text == '=':
                button.clicked.connect(_result)
            else:
                button.clicked.connect(partial(_expresion,text))

        self.mainLayout.addLayout(self.layoutButtons)


if __name__ == "__main__":
    app = QApplication()
    calculator = Calculator()
    calculator.show()
    app.exec()
