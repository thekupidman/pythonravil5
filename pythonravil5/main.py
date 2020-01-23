#!/usr/bin/env python3
# coding=utf-8

import sys
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic,QtGui
import random
import math

class Example(QWidget):

    def __init__(self):
        super().__init__()
        QWidget.__init__(self)
        self.initUI()

    def initUI(self):
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.text1 = QTextEdit(self)
        self.text2 = QTextEdit(self)
        self.btn1 = QPushButton("Выполнить", self)
        self.btn2 = QPushButton("Очистить", self)
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.label1.setGeometry(128, 13, 60, 13)
        self.label2.setGeometry(472, 13, 60, 13)
        self.text1.setGeometry(10, 32, 320, 280)
        self.text2.setGeometry(340, 32, 320, 280)
        self.btn1.setGeometry(200, 318, 130, 50)
        self.btn2.setGeometry(340, 319, 130, 50)
        self.label1.setText("Текст")
        self.label2.setText("Слова")

        self.btn1.clicked.connect(self.btn1Click)
        self.btn2.clicked.connect(self.btn2Click)

        self.setGeometry(300, 300, 692, 413)
        self.setWindowTitle('Задание 5')
        self.show()


    def btn1Click(self):
        s2 = ""
        s2 = str(self.text1.toPlainText())
        s3 = ""
        len_s = len(s2)
        c = 0
        delenie = 0
        while c < len_s:
            s3 = s3 + s2[c]
            c = c + 1
            delenie = c%60
            if delenie == 0:
                s3 = s3 + "$ \n"
                delenie == 0
                print(delenie)
        self.text2.setText(s3)

    def btn2Click(self):
        self.text2.setText("")

if __name__=='__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
