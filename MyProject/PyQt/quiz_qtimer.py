import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, QTime

# QLCDNumber 레퍼런스
# https://doc.qt.io/qt-5/qlcdnumber.html#setDigitCount


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        self.timer.setInterval(1000) #시간간격 1초
        self.timer.timeout.connect(self.timeout) #timeout 이벤트줄때 connect와 연결
        self.setWindowTitle('QTimer') #윈도우 타이틀
        self.setGeometry(100, 100, 600, 280) #윈도우 상단 100, 100, 그림의 크기 width, height

        layout = QVBoxLayout() #Layout은 BoxLayout

        self.lcd = QLCDNumber() #PyQt에서 전자시계를 표현하는 QLCD클래스      framework에 원하는 함수 있는지부터 찾아보기
        self.lcd.display('') # 디스플레이에 보이는 내용을 비움
        self.lcd.setDigitCount(8) #디지털 시계의 자리수
        subLayout = QHBoxLayout() #VBoxLayout안에 넣을 가로방향 QHBoxLayout

        self.btnStart = QPushButton("시작") #버튼 만듦
        self.btnStart.clicked.connect(self.onStartButtonClicked) #버튼이벤트 등록

        self.btnStop = QPushButton("멈춤") #멈춤 버튼 만듦
        self.btnStop.clicked.connect(self.onStopButtonClicked) # 버튼 이벤트 등록

        layout.addWidget(self.lcd) #QLCDNumber 객체화면에 등록

        subLayout.addWidget(self.btnStart) #버튼 화면에 등록
        subLayout.addWidget(self.btnStop) #버튼 화면에 등록
        layout.addLayout(subLayout) #서브 Layout 등록

        self.btnStop.setEnabled(False) #클릭시 비활성
        self.setLayout(layout)

    def onStartButtonClicked(self):
        self.timer.start() #타이머 스레드 시작
        self.btnStop.setEnabled(True) #stop버튼 활성        #  스레드 두개 생기는거 방지
        self.btnStart.setEnabled(False) #start버튼 활성

    def onStopButtonClicked(self):
        self.timer.stop() #타이머 멈춤
        self.btnStop.setEnabled(False) #stop버튼 비활성
        self.btnStart.setEnabled(True) #start버튼 활성

    def timeout(self):
        sender = self.sender() #이벤트 객체에 접근자
        currentTime = QTime.currentTime().toString("hh:mm:ss") #현재시간 표시 e.g 11:50:32
        if id(sender) == id(self.timer): #접근자와 timer가 같으면 화면에 표시
            self.lcd.display(currentTime)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())