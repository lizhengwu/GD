from PyQt5.QtWidgets import *

import UI as ui
from common import PATH
import matplotlib

# 弹框
import tkinter.messagebox
from tkinter import *
from datetime import datetime

matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from randomData import getData

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


# 创建一个matplotlib图形绘制类
class MyFigure(FigureCanvas):
    # 第一步：创建一个创建Figure
    def __init__(self, width, height, dpi):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        # 第二步：在父类中激活Figure窗口
        super(MyFigure, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
        # 第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = self.fig.add_subplot(111)


class MainDialogImgBW(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super(MainDialogImgBW, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("显示matplotlib绘制图形")
        self.setMinimumSize(0, 0)

        # 第六步：在GUI的groupBox中创建一个布局，用于添加MyFigure类的实例（即图形）后其他部件。
        # 继承容器groupBox
        self.gridlayout = QGridLayout(self.groupBox)

        # 颜色标签
        self.color_list = ['#88CCEE', '#CC6677', '#DDCC77', '#117733', '#332288', '#AA4499', '#44AA99', '#999933',
                           '#661100', '#6699CC',
                           '#888888']

        # 当前题
        self.curStep = 0
        # 路径数据
        self.pathData = getData()
        # 答案集合
        self.answerData = []

        # 初始化
        self.lastTime = 0

        # 添加答案集合
        self.comboBox.addItems(PATH)
        # 初始化什么也不选
        self.comboBox.setCurrentIndex(-1)
        # # 答案选择触发事件
        # self.comboBox.actionEvent(self.answerAction())

        self.pushButton.clicked.connect(self.nextClick)

        # 第五步：定义MyFigure类的一个实例
        # self.drawBar()
        # self.drawPie()

    # 横图
    def drawBar(self, x, y, color):
        # F = MyFigure(width=12, height=4, dpi=100)
        # F.axes.barh(x, y, color=color)
        # F.fig.suptitle("image")
        # self.gridlayout.addWidget(F, 0, 1)
        plt.figure(figsize=(12, 8), dpi=100)
        plt.barh(x, y, color=color)
        plt.yticks(x, None, rotation=45, fontsize=8)
        plt.tight_layout()
        plt.show()

    # 竖图
    def drawColumn(self, x, y, color):
        # F = MyFigure(width=12, height=4, dpi=100)
        # F.axes.bar(x, y, color=color, width=0.4)
        # F.fig.suptitle("image")
        #
        # self.gridlayout.addWidget(F, 0, 1)
        #
        # self.gridlayout.addWidget(plt.figure(), 0, 1)
        # plt.savefig('./image.png')

        plt.figure(figsize=(12, 8), dpi=100)
        plt.bar(x, y, color=color)
        plt.xticks(x, None, rotation=45, fontsize=8)
        plt.tight_layout()
        plt.show()

        # jpg = QtGui.QPixmap("./image.png").scaled(self.label_2.width(), self.label_2.height())
        # self.label_2.setPixmap(jpg)
        # self.show()

    # 饼图
    def drawPie(self, x, y):
        # F1 = MyFigure(width=12, height=4, dpi=100)
        # F1.fig.suptitle("Figuer_2")
        # F1.axes.pie(y, labels=x)
        # self.gridlayout.addWidget(F1, 0, 1)
        plt.figure(figsize=(12, 8), dpi=100)
        plt.pie(y, labels=None , colors = self.color_list)
        plt.legend(x, loc="best", fontsize=10, bbox_to_anchor=(0.1, 1))
        plt.show()
        plt.tight_layout()

    # 下一题
    def nextClick(self):

        # 校验是否选择答案
        if self.comboBox.currentIndex() == -1 and len(self.comboBox.currentText()) == 0:
            tkinter.messagebox.showinfo("提示", "咋回事？不选答案哦？")
            return

        last_time = self.lastTime
        now = datetime.now().second
        duration = now - last_time
        # _translate = QCoreApplication.translate

        if self.curStep < len(self.pathData) - 1:
            # self.pushButton_2.setVisible(True)
            self.curStep += 1

            # self.textBrowser.setText(self.pathData[self.curStep].get('target_name'))
            # self.textBrowser_2.setText(str(self.pathData[self.curStep].get('target_value')))
            # self.textBrowser_3.setText(str(self.pathData[self.curStep].get('data')))
            # self.label_5.setText("题目类型：" + self.pathData[self.curStep].get('data_type'))

            image_type = self.pathData[self.curStep].get("image_type")
            color = self.pathData[self.curStep].get("color")

            x = []
            y = []

            for item in self.pathData[self.curStep].get("data"):
                name = item.get("name")
                value = item.get("value")
                x.append(name)

                y.append(value)

            # self.drawPie(x, y)
            self.draw(image_type, color, x, y)

            self.comboBox.clear()
            self.comboBox.clearEditText()

            # 添加答案集合
            self.comboBox.addItems(PATH)
            self.comboBox.setCurrentIndex(-1)
            self.comboBox.setCurrentText('')

            # self.comboBox.clear()
            if self.curStep == 11:
                self.nextBtn.setText("submit")
        else:
            print('提交答案')

    # 画图
    def draw(self, image_type, color, x, y):
        if image_type == "bar":
            if color == 'color':
                self.drawBar(x, y, self.color_list)
            else:
                self.drawBar(x, y, None)
        if image_type == "column":
            if color == 'color':
                self.drawColumn(x, y, self.color_list)
            else:
                self.drawColumn(x, y, None)
        if image_type == "pie":
            self.drawPie(x, y)

        # if color == 'color':
        #     self.drawPie(x, y)
        # else:
        #     self.drawPie(x, y)


if __name__ == "__main__":

    tk = Tk()
    tk.withdraw()

    askyesno = tkinter.messagebox.askyesno("草拟吗", "福俺哥可和豆腐干安科技感发动机号挨个打泛华金控轧空京东方感康大家开发爱国海景房kg阿道夫")
    if askyesno:
        app = QApplication(sys.argv)
        main = MainDialogImgBW()
        main.show()
        sys.exit(app.exec_())
    else:
        tkinter.messagebox.showinfo("滚", "滚")
        sys.exc_info()
    # app.installEventFilter(main)
