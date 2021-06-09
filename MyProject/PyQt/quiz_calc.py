import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import pyqtSignal, QObject, QCoreApplication, pyqtSlot


class Communicate(QObject):

    calc_signal = pyqtSignal(int, int)
    cancel_signal = pyqtSignal()

    def run_calc(self):
        self.cancel_signal.emit(self.line_edit1.text, self.line_edit2.text)

    def run_cancel(self):
        self.cancel_signal.emit()

class CalcApp(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

        my_signal = Communicate()
        my_signal.calc_signal.connect()
        my_signal.cancel_signal.connect(QCoreApplication.instance().quit)



    def init_ui(self):
        calc_button = QPushButton('계산', self)
        cancel_button = QPushButton('cancel', self)

        calc_button.clicked.connect(self.my_signal.run_calc)
        cancel_button.clicked.connect(self.my_signal.run_cancel)

        plus_label = QLabel('+', self)
        equal_label = QLabel('=', self)

        self.line_edit1 = QLineEdit()
        self.line_edit2 = QLineEdit()
        self.line_edit3 = QLineEdit()

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.line_edit1)
        hbox1.addWidget(plus_label)
        hbox1.addWidget(self.line_edit2)
        hbox1.addWidget(equal_label)
        hbox1.addWidget(self.line_edit3)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(calc_button)
        hbox2.addWidget(cancel_button)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)

        self.setWindowTitle('plus calculation')
        self.setGeometry(500, 500, 400, 200)
        self.show()

    @pyqtSlot(int, int)
    def calculate(self, int1, int2):
        return int1 + int2

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CalcApp()
    sys.exit(app.exec_())