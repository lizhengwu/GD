#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import (
    QWidget, QDesktopWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QComboBox, QApplication)
from common import PATH
from randomData import getData

class QuestionBox(QWidget):

    def __init__(self):
        super().__init__()

        self.curStep = 0
        self.pathData = getData()
        self.initUI()

    def initUI(self):

        # 设置高度，居中展示
        self.resize(1000, 800)
        self.center()

        # Widgets
        self.prevBtn = QPushButton("Prev")
        self.nextBtn = QPushButton("Next")
        self.prevBtn.setVisible(False)

        self.targetName = QLabel("正确答案：" + self.pathData[self.curStep].get('target_name'), self)
        self.targetValue = QLabel("正确花费：" + str(self.pathData[self.curStep].get('target_value')), self)
        self.chartData = QLabel("绘图数据：" + str(self.pathData[self.curStep].get('data')), self)
        self.type = QLabel("题目类型：" + self.pathData[self.curStep].get('data_type'), self)
        self.num = QLabel("题目编号：" + str(self.curStep + 1), self)

        commboTitle = QLabel("请选择：", self)
        commbo = QComboBox(self)
        for item in PATH:
            commbo.addItem(item)

        commboTitle.move(10, 10)
        commbo.move(60, 13)

        self.targetName.setGeometry(10, 40, 900, 20)
        # self.targetValue.move(10, 60)
        self.targetValue.setGeometry(10, 60, 900, 20)
        # self.chartData.move(10, 80)
        self.chartData.setGeometry(10, 80, 900, 20)
        # self.type.move(10, 100)
        self.type.setGeometry(10, 100, 900, 20)
        self.num.setGeometry(10, 120, 900, 20)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.prevBtn)
        hbox.addWidget(self.nextBtn)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        # bind events
        self.nextBtn.clicked.connect(self.nextClick)
        self.prevBtn.clicked.connect(self.prevClick)
        commbo.activated[str].connect(self.onActivated)

        self.setWindowTitle('GD')
        self.show()

    def onActivated(self, text):
        print('选中答案：', text)

    # 下一题
    def nextClick(self):
        if self.curStep < len(self.pathData) - 1:
            self.prevBtn.setVisible(True)
            self.curStep += 1
            self.targetName.setText("正确答案：" + self.pathData[self.curStep].get('target_name'))
            self.targetValue.setText("正确花费：" + str(self.pathData[self.curStep].get('target_value')))
            self.chartData.setText("绘图数据：" + str(self.pathData[self.curStep].get('data')))
            self.type.setText("题目类型：" + self.pathData[self.curStep].get('data_type'))
            self.num.setText("题目编号：" + str(self.curStep + 1))

            if self.curStep == 11:
                self.nextBtn.setText("OK")
        else:
            print('提交答案')

    # 上一题
    def prevClick(self):
        if self.curStep > 0:
            self.curStep -= 1
            self.targetName.setText("正确答案：" + self.pathData[self.curStep].get('target_name'))
            self.targetValue.setText("正确花费：" + str(self.pathData[self.curStep].get('target_value')))
            self.chartData.setText("绘图数据：" + str(self.pathData[self.curStep].get('data')))
            self.type.setText("题目类型：" + self.pathData[self.curStep].get('data_type'))
            self.num.setText("题目编号：" + str(self.curStep + 1))
            if self.curStep == 0:
                self.prevBtn.setVisible(False)

        self.nextBtn.setText("Next")

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
