import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        Label1 = QLabel('First label', self)
        Label1.setAlignment(Qt.AlignCenter)
        Label2 = QLabel('Second label', self)

        vbox = QVBoxLayout()
        vbox.addWidget(Label1)
        vbox.addWidget(Label2)

        self.setLayout(vbox)
        self.setWindowTitle('label')
        self.setGeometry(400, 400, 400, 400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())