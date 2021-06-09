import cv2
from tensorflow.keras.models import load_model

import tensorflow as tf
import numpy as np
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap


class Video:
    def __init__(self, device = 'http://192.168.0.28:4747/video'):
        self.cap = cv2.VideoCapture(device)
        retval, self.frame = self.cap.read()
        self.save = False
        self.text = " "

    def updateFrame(self):
        if self.save == False:
            retval, self.frame = self.cap.read()
            result = self.convertCVImgToQtPixmap(self.frame)
            return result
        else:
            img = QPixmap("C:\\Users\\user\\Desktop\\image.jpg")
            return img

    def convertCVImgToQtPixmap(self, cvImg):
        if type(cvImg[0][0]) == np.uint8:
            h, w = cvImg.shape
            qImg = QtGui.QImage(cvImg.data, w, h, w, QtGui.QImage.Format_Grayscale8)
        else:
            cvImg = cv2.cvtColor(cvImg, cv2.COLOR_BGR2RGB)
            h, w, c = cvImg.shape
            qImg = QtGui.QImage(cvImg.data, w, h, w*c, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qImg)

        return pixmap

    def saveImg(self):
        cv2.imwrite("C:\\Users\\user\\Desktop\\image.jpg", self.frame)
        print("save completed")
        self.save = True
        self.trimming()

    def trimming(self):
        if self.save == True:
            img = cv2.imread("C:\\Users\\user\\Desktop\\image.jpg")
            img = img[20:, 90:550]     # from 480 X 640
            img1 = cv2.resize(img, dsize=(28, 28), interpolation=cv2.INTER_AREA)
            img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

            out = img2.copy()
            height, width = img2.shape
            high = img2.max()
            low = img2.min()

            for i in range(width):
                for j in range(height):
                    out[i][j] = ((img2[i][j] - low) * 255 / (high - low))

            cv2.imwrite("C:\\Users\\user\\Desktop\\trimmed_img.jpg", out)

        else:
            pass

    def analysis(self):
        my_model = load_model("./cnn_mnist.hdf5")
        img = cv2.imread("C:\\Users\\user\\Desktop\\trimmed_img.jpg", cv2.IMREAD_GRAYSCALE)
        img2 = 255 - img.copy()
        test_data = img2.reshape(1, 28, 28, 1).astype('float64') / 255
        result = my_model.predict_classes(test_data)
        self.text = str(result[0])
        print(result[0])

    def close(self):
        if self.cap.isOpened():
            self.cap.release()

        print("Finish Capture")