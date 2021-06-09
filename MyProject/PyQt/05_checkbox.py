import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        checkbox = QCheckBox('check 1', self)
        checkbox.move(20, 20)
        checkbox.toggle()   # default == unchecked
        checkbox.stateChanged.connect(self.change_title)

        self.setWindowTitle('Qcheckbox')
        self.setGeometry(400, 400, 400, 400)
        self.show()

    def change_title(self, state):
        if state == Qt.Checked:                    # unchecked = 0, checked = 2, partially checked = 1
            self.setWindowTitle("Qcheckbox")
        else:
            self.setWindowTitle(" ")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())