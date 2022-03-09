import sys

from PySide6 import QtWidgets
from PySide6 import QtGui, QtCore
from PySide6.QtCore import * 
from PySide6.QtGui import *
from PySide6.QtWidgets import QFileDialog, QMainWindow, QMessageBox

from generated_files.uic.mainwindow import Ui_MainWindow

import cv2
import numpy as np


class MainWindow(QMainWindow):

    def __init__(self):
        #QWidget.__init__(self)
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer=QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.cap = cv2.VideoCapture(0) # call default camera device
        self.timer.start()
    
    def display(self, frame):
        '''display frame from opencv'''
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        image = QImage(frame, frame.shape[1], frame.shape[0], 
                        frame.strides[0], QImage.Format_RGB888)
        
        self.ui.image_label.setPixmap(QPixmap.fromImage(image))

    def display_video_stream(self):
        '''Display video stream from usb camera'''
        ret, frame = self.cap.read() # get status and frame
        self.display(frame)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())