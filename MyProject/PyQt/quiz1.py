import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        btn1 = QPushButton('1', self)
        btn2 = QPushButton('2', self)

        vbox = QVBoxLayout()
        vbox.stretch(1)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.stretch(1)

        self.setLayout(vbox)

        self.setWindowTitle("quit")
        self.setGeometry(500,500,500,500)
        self.show()

        btn1.clicked.connect(self.openImage)
        btn2.clicked.connect(QCoreApplication.instance().quit)

    def openImage(self):
        src = cv2.imread('../OpenCV/data/lena.jpg')
        cv2.imshow('lena', src)
        cv2.waitKey()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
