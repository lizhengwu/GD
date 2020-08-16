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
import json


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
        # self.gridlayout = QGridLayout(self.groupBox)

        # 颜色标签
        self.color_list = ['#88CCEE', '#CC6677', '#DDCC77', '#117733', '#332288', '#AA4499', '#44AA99', '#999933',
                           '#661100', '#6699CC',
                           '#888888']
        self.color_list2 = ['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF',
                            '#FFFFFF', '#FFFFFF',
                            '#FFFFFF']

        # 当前题
        self.curStep = 0
        # 路径数据
        self.pathData = getData()
        # 答案集合
        self.answerData = []

        # 初始化
        self.lastTime = datetime.now()
        self.last_image_type = ''
        self.last_color = ''
        self.last_target_name = ''
        self.last_target_value = ''
        self.last_data = {}

        # 添加答案集合
        self.comboBox.addItems(PATH)
        # 初始化什么也不选
        self.comboBox.setCurrentIndex(-1)
        # # 答案选择触发事件
        # self.comboBox.actionEvent(self.answerAction())

        self.pushButton.clicked.connect(self.nextClick)
        self.pushButton_2.clicked.connect(self.start)

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

        if color is None:
            plt.barh(x, y, color=color)
            plt.yticks(x, None, rotation=45, fontsize=8)
        else:
            for i in range(11):
                plt.barh(x[i], y[i], color=self.color_list[i])
                plt.yticks([], None, rotation=45, fontsize=8)
                plt.legend(x, ncol=2, loc="best", fontsize=10, bbox_to_anchor=(1, 1))
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

        if color is None:
            plt.bar(x, y)
            plt.xticks(x, None, rotation=45, fontsize=8)
        else:
            for i in range(11):
                plt.bar(x[i], y[i], color=self.color_list[i])
                plt.xticks([], None, rotation=45, fontsize=8)
                plt.legend(x, ncol=2, loc="best", fontsize=10, bbox_to_anchor=(1, 1))

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
        plt.pie(y, labels=None, colors=self.color_list)
        plt.legend(x, loc="best", fontsize=10, bbox_to_anchor=(0.1, 1))
        plt.show()
        plt.tight_layout()

    # 饼图
    def drawPie2(self, x, y):
        # F1 = MyFigure(width=12, height=4, dpi=100)
        # F1.fig.suptitle("Figuer_2")
        # F1.axes.pie(y, labels=x)
        # self.gridlayout.addWidget(F1, 0, 1)
        # plt.rcParams['lines.linewidth'] = 2
        # plt.rcParams['patch.edgecolor'] = '#88CCEE'
        plt.figure(figsize=(12, 8), dpi=100)
        plt.pie(y, labels=x, colors=self.color_list2, wedgeprops={'linewidth': 3, "edgecolor": "black"})
        # plt.legend(x, loc="best", fontsize=10, bbox_to_anchor=(0.1, 1))
        plt.show()
        plt.tight_layout()

    def start(self):
        if self.curStep > 0:
            tkinter.messagebox.showinfo("提示", "已经开始答题了")
            return

        # 初始化
        self.lastTime = datetime.now()
        self.last_image_type = self.pathData[self.curStep].get("image_type")
        self.last_color = self.pathData[self.curStep].get("color")
        self.last_target_name = self.pathData[self.curStep].get("target_name")
        self.last_target_value = self.pathData[self.curStep].get("target_value")
        self.last_data = self.pathData[self.curStep]

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

        self.curStep += 1

    # 下一题
    def nextClick(self):

        if self.curStep == 0:
            tkinter.messagebox.showinfo("提示", "请点击开始")
            return

        # 校验是否选择答案
        if self.comboBox.currentIndex() == -1 and len(self.comboBox.currentText()) == 0:
            tkinter.messagebox.showinfo("提示", "咋回事？不选答案哦？")
            return

        last_time = self.lastTime
        now = datetime.now()
        duration = (now - last_time).seconds

        select = self.comboBox.currentText()
        answer = {
            'duration': duration,
            'customer_select': select,
            'last_target_name': self.last_target_name,
            'last_target_value': self.last_target_value,
            'last_image_type': self.last_image_type,
            'last_color': self.last_color,
            'last_data': self.last_data
        }
        self.answerData.append(answer)

        # _translate = QCoreApplication.translate

        if self.curStep < len(self.pathData):
            # self.pushButton_2.setVisible(True)

            self.lastTime = datetime.now()
            self.last_image_type = self.pathData[self.curStep].get("image_type")
            self.last_color = self.pathData[self.curStep].get("color")
            self.last_target_name = self.pathData[self.curStep].get("target_name")
            self.last_target_value = self.pathData[self.curStep].get("target_value")
            self.last_data = self.pathData[self.curStep]

            image_type = self.pathData[self.curStep].get("image_type")
            color = self.pathData[self.curStep].get("color")

            x = []
            y = []

            for item in self.pathData[self.curStep].get("data"):
                name = item.get("name")
                value = item.get("value")
                x.append(name)

                y.append(value)

            self.curStep += 1

            # self.drawPie(x, y)
            self.draw(image_type, color, x, y)

            # 添加答案集合
            self.comboBox.clear()
            self.comboBox.clearEditText()
            self.comboBox.addItems(PATH)
            self.comboBox.setCurrentIndex(-1)
            self.comboBox.setCurrentText('')

            # self.comboBox.clear()
            # if self.curStep == self.pathData.__len__():
            #     self.nextBtn.setText("submit")
        else:
            tkinter.messagebox.askyesno("提示", "辛苦了，答完了")
            answerData = json.dumps(self.answerData)
            txt = "./answer" + str(datetime.now()) + ".txt"
            file = open(txt, 'w')
            file.write(answerData)
            file.close()

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
            if color == "color":
                self.drawPie(x, y)
            else:
                self.drawPie2(x, y)

        # if image_type == "column":
        # self.drawBar(x, y, self.color_list)


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
