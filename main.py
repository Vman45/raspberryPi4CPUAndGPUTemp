#! /usr/bin/python3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTimer

from gpiozero import CPUTemperature
import os
import time


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Temperature'
        self.left = 20
        self.top = 40
        # set height and width
        self.width = 400
        self.height = 150
        # create labels
        self.CPULabel = QLabel(self.getCPUTemp())
        self.CPULabel.setAlignment(Qt.AlignCenter)
        self.GPULabel = QLabel(self.getGPUTemp())
        self.GPULabel.setAlignment(Qt.AlignCenter)
        # layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.CPULabel)
        vbox.addWidget(self.GPULabel)
        # creating a timer object 
        timer = QTimer(self) 
        # adding action to timer 
        timer.timeout.connect(self.updateTemp) 
        # update the timer every second 
        timer.start(1000) 
        self.setLayout(vbox)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        self.show()

    def getGPUTemp(self):
        return "GPU temp: " + os.popen("vcgencmd measure_temp").readline().replace("temp=", "")
    def getCPUTemp(self):
        return "CPU temp: " + "{:.1f}".format(CPUTemperature().temperature) + "'C"

    def updateTemp(self):
        self.CPULabel.setText(self.getCPUTemp())
        self.GPULabel.setText(self.getGPUTemp())
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
