import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MySignal(QObject):
    signal1 = pyqtSignal()              # event 하나당 하나의 시그널 객체 -> 충돌을 예방
    signal2 = pyqtSignal(int, int)

    def run(self):
        self.signal1.emit()         #signal 1, 2 라는 이름으로도 구분가능하고 매개변수의 개수와 종류로도 구분가능
        self.signal2.emit(1, 2)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        mysignal = MySignal()
        mysignal.signal1.connect(self.signal1_emitted)
        mysignal.signal2.connect(self.signal2_emitted)
        mysignal.run()

    @pyqtSlot()         # 데코레이터 (일반적으로 자질구래한 코딩 축약을 위해 사용)
    def signal1_emitted(self):
        print("signal1 emitted")

    @pyqtSlot(int, int)    # type을 강제로 지정, 정수타입 두개가 안들어오면 실행안됨
    def signal2_emitted(self, arg1, arg2):
        print("signal2 emitted", arg1, arg2)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()