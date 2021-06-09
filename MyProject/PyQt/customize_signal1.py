import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MySignal(QObject):        # 이벤트 처리 클래스
    signal1 = pyqtSignal()

    def run(self):
        self.signal1.emit()     # 메세지를 던짐, 운영체제 queue에 들어가기 때문에 동시에 접근할 경우 충돌나는걸 방지


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        mysignal = MySignal()
        mysignal.signal1.connect(self.signal1_emitted)
        mysignal.run()

    @pyqtSlot()     # 매개변수 없음을 강조 , 시그널과 슬롯을 연결할 때 데코레이터를 사용하는 것을 권장 (함수 중복 방지)
    def signal1_emitted(self):
        print("signal1 emitted")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()