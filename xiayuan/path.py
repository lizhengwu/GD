# Module importantions
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
import random
import numpy as np
import os
from faker import Faker
from faker.providers import BaseProvider
import matplotlib.pyplot as plt
import time
from collections import Counter

class Timer(object):
    def __init__(self):
        self.time_arr = []

    def compute_time(self):
        self.start_time = time.time()

    def compute_time2(self):
        self.end_time = time.time()
        self.time_arr.append(self.end - self.start)
        print(self.end_time - self.start_time)
        print(self.time_arr)
        np.savetxt('Timer.csv', self.time_arr, delimiter=',')


# Generating patients' outcomes using the baseprovider faker constructor
class MyProvider(BaseProvider):
    def Outcome(self):
        self.rand_int = random.randint(1, 100)
        # Assigning different outcomes with different IDs
        if self.rand_int <= 52:
            self.outcome_id = 1  # Admitted
        elif self.rand_int >= 53 and self.rand_int <= 57:
            self.outcome_id = 2  # Call Closed
        elif self.rand_int > 57 and self.rand_int <= 64:
            self.outcome_id = 3  # Discharged
        elif self.rand_int > 64 and self.rand_int <= 68:
            self.outcome_id = 4  # Emergency dentist
        elif self.rand_int > 68 and self.rand_int <= 76:
            self.outcome_id = 5  # MIU
        elif self.rand_int > 76 and self.rand_int <= 81:
            self.outcome_id = 6  # Not picked up in an ambulance
        elif self.rand_int > 81 and self.rand_int <= 82:
            self.outcome_id = 7  # OOH
        elif self.rand_int > 82 and self.rand_int <= 83:
            self.outcome_id = 8  # Out-patient clinic
        elif self.rand_int > 83 and self.rand_int <= 85:
            self.outcome_id = 9  # Seen by A&E doctor
        elif self.rand_int > 85 and self.rand_int <= 88:
            self.outcome_id = 10  # Spoke to a primary care service
        else:
            self.outcome_id = 11  # WIC
        return self.outcome_id

    def Random_cost_time(self):
        self.outcome_id = MyProvider.Outcome(MyProvider)
        # Calculating random time for each outcome
        a = random.randint(10, 20)
        b = random.randint(20, 25)
        c = random.randint(15, 19)
        d = random.randint(18, 20)
        e = random.randint(35, 39)
        f = random.randint(46, 52)
        g = random.randint(36, 40)

        # time and cost generators
        if self.outcome_id == 1:
            self.unit_time = a + b + d + e + f + g  # ADMITTED
            self.unit_cost = random.randint(500, 1200)
        elif self.outcome_id == 2:
            self.unit_time = a + b + d  # CALL_CLOSED
            self.unit_cost = random.randint(8, 14)
        elif self.outcome_id == 3:
            self.unit_time = a + b + c + e  # DISCHARGED
            self.unit_cost = random.randint(200, 350)
        elif self.outcome_id == 4:
            self.unit_time = a + b + e  # EMMERGENCY DENTIST
            self.unit_cost = random.randint(20, 80)
        elif self.outcome_id == 5:
            self.unit_time = a + b + d + e + f  # MIU
            self.unit_cost = random.randint(70, 195)
        elif self.outcome_id == 6:
            self.unit_time = a + c + g  # NOT PICKED
            self.unit_cost = random.randint(20, 80)
        elif self.outcome_id == 7:
            self.unit_time = a + c + d  # OOH
            self.unit_cost = random.randint(120, 260)
        elif self.outcome_id == 8:
            self.unit_time = a + c + e  # OUT_PATIENT CLINIC
            self.unit_cost = random.randint(350, 750)
        elif self.outcome_id == 9:
            self.unit_time = a + c  # SEEN BY A&E DOCTOR
            self.unit_cost = random.randint(300, 700)
        elif self.outcome_id == 10:
            self.unit_time = a + b + g  # PRIMARY CARE SERVICE
            self.unit_cost = random.randint(20, 80)
        else:
            self.unit_time = a + b + f + g  # WIC
            self.unit_cost = random.randint(12, 16)
        return self.outcome_id, self.unit_time, self.unit_cost

    def Creation(self):
        the_row = 500
        the_column = 3
        FakerData = np.zeros([the_row, the_column])
        for i in range(the_row):
            Outcome, Time, Cost = MyProvider.Random_cost_time(MyProvider)
            one_record = [Outcome, Time, Cost]
            for j in range(the_column):
                FakerData[i][j] = one_record[j]
        np.savetxt('SimulatedData.csv', FakerData, delimiter=',')

fake = Faker()
fake.add_provider(MyProvider)  # add this class to Faker
fake.Creation()

The_data = np.loadtxt(open('SimulatedData.csv', 'rb'), delimiter=',', skiprows=0)
Outcome = The_data[:, 0]
Outcome = Outcome.astype(int)
Time = The_data[:, 1]
Cost = The_data[:, 2]
Outcome_Frequency = np.bincount(Outcome)
Total_Cost_List = np.zeros([11, 1])
Average_Cost_List = np.zeros([11, 1])

for i in range(500):
    for j in range(1, 12):
        if Outcome[i] == j:
            one_cost = Cost[i]
            Total_Cost_List[j - 1] = Total_Cost_List[j - 1] + one_cost

for i in range(len(Outcome_Frequency) - 1):
    Average_Cost_List[i] = Total_Cost_List[i] / Outcome_Frequency[i + 1]


class Graph(object):
    def TheBarChart1(self):
        self.input_list = Average_Cost_List
        self.name_list = ['Admitted', 'Call Closed', 'Discharged', 'Emergency dentist', 'MIU',
                          'Not picked up in an ambulance', 'OOH', 'Out-patient clinic', 'Seen by A&E doctor',
                          'Spoke to a primary care service', 'WIC']
        self.colors = ['CornflowerBlue', 'CornflowerBlue', 'CornflowerBlue', 'CornflowerBlue', 'CornflowerBlue',
                       'CornflowerBlue', 'CornflowerBlue', 'CornflowerBlue', 'CornflowerBlue', 'CornflowerBlue',
                       'CornflowerBlue']
        self.BC2 = plt.figure(figsize=(14, 8))
        self.BC2_chart = self.BC2.add_subplot(1, 2, 1)
        self.BC2_legend = self.BC2.add_subplot(1, 2, 2)

        self.BC2_chart.set_title('Average Cost in Different Outcomes')
        self.BC2_chart.set_xlabel('Outcome')
        self.BC2_chart.set_ylabel('Average Cost(GBP)')
        self.BC2_chart.set_xticks(range(len(self.name_list)))

        for i in range(len(Average_Cost_List)):
            self.BC2_chart.bar(i, self.input_list[i], color=self.colors[i], width=0.7)

        self.BC2_ysuitrange_list = []
        for a, b in zip(range(len(Average_Cost_List)), self.input_list):
            self.BC2_chart.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)
            self.BC2_barnumber = [a]
            self.BC2_xsuitrange = [a - 0.5, a + 0.5]
            self.BC2_ysuitrange = [0, b]
            self.BC2_ysuitrange_list.append(b)

        self.img = Image.open('bar_graph_1.png')
        self.BC2_legend.axis('off')
        self.BC2_legend.imshow(self.img)

        plt.show()
        return ()

    def ThePieChart1(self):
        # generating pie chart with numbers and completely different colors
        self.input_list = Total_Cost_List.flatten()
        self.name_list = ['1 Admitted', '2 Call Closed', '3 Discharged', '4 Emergency dentist', '5 MIU',
                          '6 Not picked up in an ambulance', '7 OOH', '8 Out-patient clinic', '9 Seen by A&E doctor',
                          '10 Spoke to a primary care service', '11 WIC']
        self.colors = ['slateblue', 'orange', 'g', 'r', 'purple', 'brown', 'pink', 'gray', 'yellow', 'aqua',
                       'lightskyblue']
        self.PC1 = plt.figure(figsize=(14, 8))
        self.PC1_chart = self.PC1.add_subplot(1, 2, 1)
        self.PC1_chart = plt.pie(self.input_list,
                                 startangle=90,
                                 shadow=True,
                                 colors=self.colors
                                 )
        plt.title('Different outcomes cost percentage of total cost', fontdict={'weight': 'normal', 'size': 12})
        plt.axis('off')
        plt.legend(bbox_to_anchor=(1, 1),
                   loc='center right',
                   bbox_transform=plt.gcf().transFigure)

        self.img = Image.open('pie_graph.png')
        self.PC1_legend = self.PC1.add_subplot(1, 2, 2)
        self.PC1_legend.axis('off')
        self.PC1_legend.imshow(self.img)

        plt.show()
        return ()

    def TheBarChart2(self):
        # generating bar chart
        self.input_list = Average_Cost_List
        self.name_list = ['Admitted', 'Call Closed', 'Discharged', 'Emergency dentist', 'MIU',
                          'Not picked up in an ambulance', 'OOH', 'Out-patient clinic', 'Seen by A&E doctor',
                          'Spoke to a primary care service', 'WIC']
        self.colors = ['midnightblue', 'mediumblue', 'blue', 'dodgerblue', 'lightblue', 'PowderBlue', 'lightsteelblue',
                       'lightskyblue', 'CornflowerBlue', 'steelBlue', 'slateBlue']
        self.BC2 = plt.figure(figsize=(14, 8))
        self.BC2_chart = self.BC2.add_subplot(1, 2, 1)
        self.BC2_legend = self.BC2.add_subplot(1, 2, 2)

        self.BC2_chart.set_title('Average Cost in Different Outcomes')
        self.BC2_chart.set_xlabel('Outcome')
        self.BC2_chart.set_ylabel('Average Cost(GBP)')
        self.BC2_chart.set_xticks(range(len(self.name_list)))

        for i in range(len(Average_Cost_List)):
            self.BC2_chart.bar(i, self.input_list[i], color=self.colors[i], width=0.7)

        self.BC2_ysuitrange_list = []
        for a, b in zip(range(len(Average_Cost_List)), self.input_list):
            self.BC2_chart.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)
            self.BC2_barnumber = [a]
            self.BC2_xsuitrange = [a - 0.5, a + 0.5]
            self.BC2_ysuitrange = [0, b]
            self.BC2_ysuitrange_list.append(b)

        self.img = Image.open('bar_graph_2.png')
        self.BC2_legend.axis('off')
        self.BC2_legend.imshow(self.img)

        plt.show()
        return ()

    def TheBarChart3(self):
        # generating bar chart
        self.input_list = Average_Cost_List
        self.name_list = ['Admitted', 'Call Closed', 'Discharged', 'Emergency dentist', 'MIU',
                          'Not picked up in an ambulance', 'OOH', 'Out-patient clinic', 'Seen by A&E doctor',
                          'Spoke to a primary care service', 'WIC']
        self.colors = ['midnightblue', 'mediumblue', 'blue', 'dodgerblue', 'lightblue', 'PowderBlue', 'lightsteelblue',
                       'lightskyblue', 'CornflowerBlue', 'steelBlue', 'slateBlue']
        self.BC2 = plt.figure(figsize=(14, 8))
        self.BC2_chart = self.BC2.add_subplot(1, 2, 1)
        self.BC2_legend = self.BC2.add_subplot(1, 2, 2)

        self.BC2_chart.set_title('Average Cost in Different Outcomes')
        self.BC2_chart.set_xlabel('Outcome')
        self.BC2_chart.set_ylabel('Average Cost(GBP)')
        self.BC2_chart.set_xticks(range(len(self.name_list)))

        for i in range(len(Average_Cost_List)):
            self.BC2_chart.bar(i, self.input_list[i], color=self.colors[i], width=0.7)

        self.BC2_ysuitrange_list = []
        for a, b in zip(range(len(Average_Cost_List)), self.input_list):
            self.BC2_barnumber = [a]
            self.BC2_xsuitrange = [a - 0.5, a + 0.5]
            self.BC2_ysuitrange = [0, b]
            self.BC2_ysuitrange_list.append(b)

        self.img = Image.open('bar_graph_2.png')
        self.BC2_legend.axis('off')
        self.BC2_legend.imshow(self.img)

        plt.show()
        return ()

    def ThePieChart2(self):
        self.input_list = Total_Cost_List.flatten()
        self.name_list = ['1 Admitted', '2 Call Closed', '3 Discharged', '4 Emergency dentist', '5 MIU',
                          '6 Not picked up in an ambulance', '7 OOH', '8 Out-patient clinic', '9 Seen by A&E doctor',
                          '10 Spoke to a primary care service', '11 WIC']
        self.colors = ['midnightblue', 'mediumblue', 'blue', 'dodgerblue', 'lightblue', 'PowderBlue', 'lightsteelblue',
                       'lightskyblue', 'CornflowerBlue', 'steelBlue', 'slateBlue']
        self.PC1 = plt.figure(figsize=(14, 8))
        self.PC1_chart = self.PC1.add_subplot(1, 2, 1)
        self.PC1_chart = plt.pie(self.input_list,
                                 startangle=90,
                                 shadow=True,
                                 colors=self.colors
                                 )
        plt.title('Different outcomes cost percentage of total cost', fontdict={'weight': 'normal', 'size': 12})
        plt.axis('off')
        plt.legend(bbox_to_anchor=(1, 1),
                   loc='center right',
                   bbox_transform=plt.gcf().transFigure)

        self.img = Image.open('bar_graph_2.png')
        self.PC1_legend = self.PC1.add_subplot(1, 2, 2)
        self.PC1_legend.axis('off')
        self.PC1_legend.imshow(self.img)

        plt.show()
        return ()

    def TheBoxPlot(self):
        self.boxplot_array = np.zeros([5, 11])
        self.calculation_list = []
        self.calculated_list = []
        self.BP2 = plt.figure(figsize=(14, 8))
        self.BP2_chart = self.BP2.add_subplot(1, 2, 1)
        self.BP2_legend = self.BP2.add_subplot(1, 2, 2)
        for i in range(1, 12):
            for j in range(500):
                if Outcome[j] == i:
                    self.calculation_list.append(Cost[j])
            self.calculated_list = np.percentile(self.calculation_list, [0, 25, 50, 75, 100])
            self.calculation_list = []
            for k in range(5):
                self.boxplot_array[k, i - 1] = self.calculated_list[k]
        self.BP2_chart.set_xlabel('Outcome')
        self.BP2_chart.set_ylabel('One Record Cost(GBP)')
        self.BP2_chart.set_title('One Time Cost Distribution')
        self.BP2_ysuitrange_listmax = []
        self.BP2_ysuitrange_listmin = []
        self.BP2_chart.boxplot(self.boxplot_array, widths=1)
        for a, b in zip(range(len(Outcome_Frequency) - 1), self.boxplot_array[4, :]):
            self.BP2_chart.text(a + 1, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)

        self.img = Image.open('key.png')
        self.BP2_legend.axis('off')
        self.BP2_legend.imshow(self.img)

        plt.show()
        return ()

    def onclick_BC1(event):
        a, b = Graph.TheBarChart1
        plt.close()


    def onclick_BC2(event):
        a, b = Graph.TheBarChart2(Graph)
        plt.close()


    def onclick_PC1(event):
        a, b = Graph.ThePieChart1(Graph)
        plt.close()


    def onclick_BP2(self, event):
        a, b = Graph.TheBoxPlot(Graph)
        plt.close()


    def onclick_BC3(event):
        a, b = Graph.TheBarChart3(Graph)
        plt.close()

    def onclick_PC2(event):
        a, b = Graph.ThePieChart2(Graph)



class Ui_MainWindow(object):
    def __init__(self):
        self.assessment = Timer()

    def setupUi(self, MainWindow):
        # MainWindow.setStyleSheet("background:#06060B;color:#ccd6f6;border:1px solid #37BB70;")
        MainWindow.setObjectName("Healthcare Pathways")
        MainWindow.resize(680, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        qli1 = self.label = QtWidgets.QLabel(self.centralwidget)
        qli1.move(150, 30)
        font = QtGui.QFont('Times')
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        font = QtGui.QFont('Times')
        font.setPointSize(12)
        font = QtGui.QFont('Times')
        font.setPointSize(12)
        qli4 = self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        qli4.move(100, 100)
        font = QtGui.QFont('Times')
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_3.addWidget(self.pushButton_10, 3, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_3.addWidget(self.pushButton_8, 2, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_3.addWidget(self.pushButton_7, 2, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_3.addWidget(self.pushButton_9, 3, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_3.addWidget(self.pushButton_11, 4, 0, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_3.addWidget(self.pushButton_13, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 2)
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_3.addWidget(self.pushButton_12, 5, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(50, 50, 500, 50))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSimulating_Data = QtWidgets.QAction(MainWindow)
        self.actionSimulating_Data.setObjectName("actionSimulating_Data")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.action1_Outcome_Distribution = QtWidgets.QAction(MainWindow)
        self.action1_Outcome_Distribution.setObjectName("action1_Outcome_Distribution")
        self.action2_Cost_in_Healthcare_Pathway = QtWidgets.QAction(MainWindow)
        self.action2_Cost_in_Healthcare_Pathway.setObjectName("action2_Cost_in_Healthcare_Pathway")

        self.retranslateUi(MainWindow)

        self.pushButton_7.clicked.connect(graph.TheBarChart1)
        self.pushButton_7.clicked.connect(self.assessment.compute_time)

        self.pushButton_8.clicked.connect(graph.ThePieChart1)
        self.pushButton_8.clicked.connect(self.assessment.compute_time)

        self.pushButton_9.clicked.connect(graph.TheBarChart2)
        self.pushButton_9.clicked.connect(self.assessment.compute_time)

        self.pushButton_10.clicked.connect(graph.ThePieChart2)  # REPLACE WITH BOX PLOT
        self.pushButton_10.clicked.connect(self.assessment.compute_time)

        self.pushButton_11.clicked.connect(graph.TheBarChart3)
        self.pushButton_11.clicked.connect(self.assessment.compute_time)

        self.pushButton_13.clicked.connect(graph.TheBoxPlot)
        self.pushButton_13.clicked.connect(self.assessment.compute_time)

        self.pushButton_12.clicked.connect(self.assessment.compute_time2)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def opennvcsv(self):
        The_data = np.loadtxt(open('model_netimis.csv', 'r'), delimiter=',', skiprows=0, dtype=str)
        np.set_printoptions(threshold=np.inf)
        print(The_data)

    def openovcsv(self):
        The_data = np.loadtxt(open('faker_model.csv', 'r'), delimiter=',', skiprows=0, dtype=str)
        np.set_printoptions(threshold=np.inf)
        print(The_data)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Visualizing Healthcare Pathways", "Visualizing Healthcare Pathways"))
        self.label.setText(_translate("MainWindow", "Visualizing the average cost of different outcomes"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Pathway Assessment and Visualization"))
        self.pushButton_10.setText(_translate("MainWindow", "Pie Charts 2"))
        self.pushButton_8.setText(_translate("MainWindow", "Pie Charts 1"))
        self.pushButton_7.setText(_translate("MainWindow", "Bar Chart 1"))
        self.pushButton_9.setText(_translate("MainWindow", "Bar Chart 2"))
        self.pushButton_11.setText(_translate("MainWindow", "Bar Chart 3"))
        self.pushButton_13.setText(_translate("MainWindow", "Box-Plot Graph"))
        self.label_4.setText(_translate("MainWindow", "Running time of finding maximum and minimum "))
        self.pushButton_12.setText(_translate("MainWindow", "Stop"))
        self.actionSimulating_Data.setText(_translate("MainWindow", "Simulating Data"))
        self.actionOpen.setText(_translate("MainWindow", "Open Data"))
        self.action1_Outcome_Distribution.setText(_translate("MainWindow", "1. Outcome Distribution"))
        self.action2_Cost_in_Healthcare_Pathway.setText(_translate("MainWindow", "2. Cost in Healthcare Pathway"))


if __name__ == "__main__":
    import sys

    fake = Faker()
    fake.add_provider(MyProvider)
    fake.Creation()
    graph = Graph()
    assessment = Timer()
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
