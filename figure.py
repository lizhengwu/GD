from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import numpy as np
import UI as ui

import matplotlib

matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from randomData import getData


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

        self.curStep = 0
        self.pathData = getData()

        self.pushButton.clicked.connect(self.nextClick)
        # self.initUI()

        # 第五步：定义MyFigure类的一个实例
        # self.drawBar()
        # self.drawPie()

    def drawBar(self, x, y):
        F = MyFigure(width=3, height=3, dpi=100)

        # x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # y = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        name_list = ['Admitted', 'Call Closed', 'Discharged', 'Emergency dentist', 'MIU',
                     'Not picked up in an ambulance', 'OOH', 'Out-patient clinic', 'Seen by A&E doctor']
        x2 = ['Admitted']
        y2 = [9 * 1.2]

        F.axes.bar(x, y)
        F.axes.bar(x2, y2)
        # F.axes.legend(name_list, loc='best')
        F.fig.suptitle("image")

        self.gridlayout.addWidget(F, 0, 1)

    def drawPie(self):
        F1 = MyFigure(width=4, height=4, dpi=100)
        F1.fig.suptitle("Figuer_2")
        # F1.axes = F1.fig.add_subplot(111)

        y = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        name_list = ['Admitted', 'Call Closed', 'Discharged', 'Emergency dentist', 'MIU',
                     'Not picked up in an ambulance', 'OOH', 'Out-patient clinic', 'Seen by A&E doctor']
        x2 = ['Admitted']
        y2 = [9 * 1.2]

        F1.axes.pie(y, labels=name_list)
        # F.axes.legend(name_list, loc='best')

        # F1.axes2 = F1.fig.add_subplot(222)
        #
        # ## 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法
        # x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # y = [23, 21, 32, 13, 3, 132, 13, 3, 1]
        # F1.axes2.plot(x, y)
        # F1.axes2.set_title("line")
        # # 散点图
        # F1.axes3 = F1.fig.add_subplot(223)
        # F1.axes3.scatter(np.random.rand(20), np.random.rand(20))
        # F1.axes3.set_title("scatter")
        # # 折线图
        # F1.axes4 = F1.fig.add_subplot(224)
        # x = np.arange(0, 5, 0.1)
        # F1.axes4.plot(x, np.sin(x), x, np.cos(x))
        # F1.axes4.set_title("sincos")

        self.gridlayout.addWidget(F1, 0, 2)

    # 下一题
    def nextClick(self):
        _translate = QCoreApplication.translate

        if self.curStep < len(self.pathData) - 1:
            self.pushButton_2.setVisible(True)
            self.curStep += 1

            self.textBrowser.setText(self.pathData[self.curStep].get('target_name'))
            self.textBrowser_2.setText(str(self.pathData[self.curStep].get('target_value')))
            self.textBrowser_3.setText(str(self.pathData[self.curStep].get('data')))

            # self.label_4.setText(str(self.pathData[self.curStep].get('data')))
            self.label_5.setText("题目类型：" + self.pathData[self.curStep].get('data_type'))
            # self.label_5.setText("题目编号：" + str(self.curStep + 1))

            x = []
            y = []

            for item in self.pathData[self.curStep].get("data"):
                name = item.get("name")
                value = item.get("value")
                x.append(name)

                y.append(value)

            self.drawBar(x, y)
            if self.curStep == 11:
                self.nextBtn.setText("OK")
        else:
            print('提交答案')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainDialogImgBW()
    main.show()
    # app.installEventFilter(main)
    sys.exit(app.exec_())
