import sys
import threading
import time
from PyQT_frame import AnalyzerUI
from CV_video import Video
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
ex = AnalyzerUI()
v = Video()

def run():
    t = 0
    while t < 2000:
        ex.video_label.setPixmap(v.updateFrame())
        ex.text_label.setText(v.text)
        time.sleep(0.01)
        t += 1

    v.close()

ex.capture_btn.clicked.connect(v.saveImg)
ex.analysis_btn.clicked.connect(v.analysis)
th = threading.Thread(target=run)
th.start()

sys.exit(app.exec_())
