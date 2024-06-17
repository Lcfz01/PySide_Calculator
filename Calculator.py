from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QLineEdit, QWidget, QGridLayout


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

    def _createDisplay(self):
        self._input = QLineEdit()
        self._input.setFixedHeight(35)
        self._input.setAlignment(Qt.AlignRight)
        self._input.setReadOnly(True)
        self.mainLayout.addWidget(self._input)

    def _createButtons(self):
        self.botones = {}
        self.layoutButtons = QGridLayout()
        #text-position
        self.botones={
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

if __name__ == "__main__":
    app = QApplication()
    calculator = Calculator()
    calculator.show()
    app.exec()
