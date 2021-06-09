import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import QTimer, QTime


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.init_ui()

    def init_ui(self):
        self.time_label = QLabel("{0:02} : {1:02} : {2:02}".format(self.hour, self.minute, self.second), self)
        self.time_label.setFont(QFont('Times', 100, weight=QFont.Bold))

        start_button = QPushButton('시작', self)
        start_button.setMaximumHeight(70)
        start_button.setMaximumWidth(500)
        start_button.setFont(QFont('Times', 25, weight=QFont.Bold))

        stop_button = QPushButton('멈춤', self)
        stop_button.setMaximumHeight(70)
        stop_button.setMaximumWidth(500)
        stop_button.setFont(QFont('Times', 25, weight=QFont.Bold))

        hbox = QHBoxLayout()
        hbox.addWidget(start_button)
        hbox.addWidget(stop_button)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.setWindowTitle("clock")
        self.setGeometry(800, 500, 700, 500)
        self.show()

        start_button.clicked.connect(self.start_timer)
        stop_button.clicked.connect(self.stop_timer)

    def print_time(self):
        time_var = QTime.currentTime()
        self.hour = time_var.hour()
        self.minute = time_var.minute()
        self.second = time_var.second()

        self.time_label.setText("{0:02} : {1:02} : {2:02}".format(self.hour, self.minute, self.second))

    def start_timer(self):
        self.timer_var = QTimer(self)
        self.timer_var.setInterval(1000)
        self.timer_var.start()
        self.timer_var.timeout.connect(self.print_time)

    def stop_timer(self):
        self.timer_var.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())