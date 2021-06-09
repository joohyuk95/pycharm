## Ex 7-5. 사용자 정의 시그널.

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow


class Communicate(QObject):

    closeApp = pyqtSignal()         # 사용자 정의 시그널 생성


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()      # 사용자 정의 시그널 사용위해 객체 생성
        self.c.closeApp.connect(self.close)         # 사용자 정의 시그널 발생시 연결될 슬롯 ( 종료 )

        self.setWindowTitle('Emitting Signal')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def mousePressEvent(self, e):       # 마우스 누르면 사용자 정의 시그널이 발행됨
        self.c.closeApp.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())