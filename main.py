#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import (
    QWidget, QDesktopWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QApplication)
from PyQt5.QtGui import QFont
from common import STEP


class QuestionBox(QWidget):

    def __init__(self):
        super().__init__()

        self.curStep = 1
        self.initUI()

    def initUI(self):
        self.title = 'Question: '

        # 设置高度，居中展示
        self.resize(1000, 800)
        self.center()

        # Widgets
        self.prevBtn = QPushButton("Prev")
        self.nextBtn = QPushButton("Next")
        self.label = QLabel(self.title + str(self.curStep), self)

        self.label.setFont(QFont('Arial', 20))
        self.label.setGeometry(20, 20, 200, 20)

        hbox = QHBoxLayout()
        hbox.addWidget(self.prevBtn)
        hbox.addWidget(self.nextBtn)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        # bind events
        self.nextBtn.clicked.connect(self.nextClick)

        self.setWindowTitle('GD')
        self.show()

    def nextClick(self):
        if self.curStep < STEP:
            self.curStep += 1
        else:
            self.curStep = 1

        self.label.setText(self.title + str(self.curStep))

    # 居中显示
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    qb = QuestionBox()
    sys.exit(app.exec_())
