# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QThread


class Cal(QThread):
    sum_signal = pyqtSignal(float)

    def run(self):
        sum = 0
        for i in range(1, 20):
            sum += i

        self.sum_signal.emit(sum)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 500)
        self.setWindowTitle('Test Signal')

        # 시그널 객체 생성
        self.btn_signal = QPushButton('시그널시작', self)
        self.btn_signal.clicked.connect(self.process_call)

        # 클래스 시그널 연결
        self.cal = Cal()
        self.cal.sum_signal.connect(self.process_sum)

    def process_call(self):
        self.cal.start()

    @pyqtSlot(float)
    def process_sum(self, float_data):
        print('return data : ', float_data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())