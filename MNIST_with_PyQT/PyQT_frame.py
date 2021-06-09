import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit


class AnalyzerUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.video_label = QLabel(self)
        self.text_label = QLabel(" ", self)
        self.capture_btn = QPushButton("Capture")
        self.analysis_btn = QPushButton("Analysis")

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.capture_btn)
        self.hbox.addWidget(self.analysis_btn)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.video_label)
        self.vbox.addWidget(self.text_label)
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)
        self.resize(400, 400)
        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = AnalyzerUI()
    sys.exit(app.exec_())
