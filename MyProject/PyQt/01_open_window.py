import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):       # QWidget 상속

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My first Application')
        self.setWindowIcon(QIcon('web.png'))
        self.move(1500, 400)
        self.resize(400, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)        #
    ex = MyApp()
    sys.exit(app.exec_())