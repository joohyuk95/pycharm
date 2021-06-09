import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.label = QLabel(self)
        self.label.move(60, 40)

        le = QLineEdit(self)
        le.move(60, 100)
        le.textChanged[str].connect(self.onChanged)

        self.setWindowTitle("QlineEdit")
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def onChanged(self, text):
        self.label.setText(text)
        self.label.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())