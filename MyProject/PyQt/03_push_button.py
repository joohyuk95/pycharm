import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        Button1 = QPushButton('btn1', self)
        Button1.setCheckable(True)      # like checkbox
        Button1.toggle()

        Button2 = QPushButton(self)
        Button2.setText('btn2')

        Button3 = QPushButton('btn3', self)
        Button3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.stretch(1)
        vbox.addWidget(Button1)
        vbox.addWidget(Button2)
        vbox.addWidget(Button3)
        vbox.stretch(1)

        self.setLayout(vbox)
        self.setWindowTitle('push button')
        self.setGeometry(800, 500, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())



