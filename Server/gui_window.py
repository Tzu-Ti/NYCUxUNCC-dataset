# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, qRgb
class Ui_MainWindow(object):
    def setUpIcon(self):
        self.node_icon = []
        self.local_icon = QtWidgets.QGraphicsView(self.centralwidget)
        self.local_icon.setGeometry(QtCore.QRect(50, 20, 131, 131))
        self.local_icon.setObjectName("local_icon")
        self.local_scene = QtWidgets.QGraphicsScene()
        self.local_scene.setSceneRect(0, 0, 121, 121)
        self.local_scene.setBackgroundBrush(QColor(qRgb(200, 255, 200)))
        self.local_icon.setScene(self.local_scene)
        self.node0_icon = QtWidgets.QGraphicsView(self.centralwidget)
        self.node0_icon.setGeometry(QtCore.QRect(230, 20, 131, 131))
        self.node0_icon.setObjectName("node0_icon")
        self.node0_scene = QtWidgets.QGraphicsScene()
        self.node0_scene.setSceneRect(0, 0, 121, 121)
        self.node0_scene.setBackgroundBrush(QColor(qRgb(255, 200, 200)))
        self.node0_icon.setScene(self.node0_scene)
        self.node_icon.append(self.node0_scene)
        self.node1_icon = QtWidgets.QGraphicsView(self.centralwidget)
        self.node1_icon.setGeometry(QtCore.QRect(410, 20, 131, 131))
        self.node1_icon.setObjectName("node1_icon")
        self.node1_scene = QtWidgets.QGraphicsScene()
        self.node1_scene.setSceneRect(0, 0, 121, 121)
        self.node1_scene.setBackgroundBrush(QColor(qRgb(255, 200, 200)))
        self.node1_icon.setScene(self.node1_scene)
        self.node_icon.append(self.node1_scene)
        self.node2_icon = QtWidgets.QGraphicsView(self.centralwidget)
        self.node2_icon.setGeometry(QtCore.QRect(590, 20, 131, 131))
        self.node2_icon.setObjectName("node2_icon")
        self.node2_scene = QtWidgets.QGraphicsScene()
        self.node2_scene.setSceneRect(0, 0, 121, 121)
        self.node2_scene.setBackgroundBrush(QColor(qRgb(255, 200, 200)))
        self.node2_icon.setScene(self.node2_scene)
        self.node_icon.append(self.node2_scene)
        self.node3_icon = QtWidgets.QGraphicsView(self.centralwidget)
        self.node3_icon.setGeometry(QtCore.QRect(770, 20, 131, 131))
        self.node3_icon.setObjectName("node3_icon")
        self.node3_scene = QtWidgets.QGraphicsScene()
        self.node3_scene.setSceneRect(0, 0, 121, 121)
        self.node3_scene.setBackgroundBrush(QColor(qRgb(255, 200, 200)))
        self.node3_icon.setScene(self.node3_scene)
        self.node_icon.append(self.node3_scene)
        self.node4_icon = QtWidgets.QGraphicsView(self.centralwidget)
        self.node4_icon.setGeometry(QtCore.QRect(950, 20, 131, 131))
        self.node4_icon.setObjectName("node4_icon")
        self.node4_scene = QtWidgets.QGraphicsScene()
        self.node4_scene.setSceneRect(0, 0, 121, 121)
        self.node4_scene.setBackgroundBrush(QColor(qRgb(255, 200, 200)))
        self.node4_icon.setScene(self.node4_scene)
        self.node_icon.append(self.node4_scene)
        
        self.node5_icon = QtWidgets.QGraphicsView(self.centralwidget)
        self.node5_icon.setGeometry(QtCore.QRect(1130, 20, 131, 131))
        self.node5_icon.setObjectName("node5_icon")
        self.node5_scene = QtWidgets.QGraphicsScene()
        self.node5_scene.setSceneRect(0, 0, 121, 121)
        self.node5_scene.setBackgroundBrush(QColor(qRgb(255, 200, 200)))
        self.node5_icon.setScene(self.node5_scene)
        self.node_icon.append(self.node5_scene)



    def setUpNodeInfo(self):
        self.node_info = [{}, {}, {}, {}, {}, {}]
        self.local_nodename = QtWidgets.QLabel(self.centralwidget)
        self.local_nodename.setGeometry(QtCore.QRect(50, 150, 131, 20))
        self.local_nodename.setObjectName("local_nodename")
        self.local_ip = QtWidgets.QLabel(self.centralwidget)
        self.local_ip.setGeometry(QtCore.QRect(50, 170, 131, 20))
        self.local_ip.setObjectName("local_ip")
        self.local_mode = QtWidgets.QLabel(self.centralwidget)
        self.local_mode.setGeometry(QtCore.QRect(50, 190, 131, 20))
        self.local_mode.setObjectName("local_mode")
        self.local_con = QtWidgets.QLabel(self.centralwidget)
        self.local_con.setGeometry(QtCore.QRect(50, 210, 131, 20))
        self.local_con.setObjectName("local_con")
        self.node0_ip = QtWidgets.QLabel(self.centralwidget)
        self.node0_ip.setGeometry(QtCore.QRect(230, 170, 131, 20))
        self.node0_ip.setObjectName("node0_ip")
        self.node_info[0]['ip'] = self.node0_ip
        self.node0_con = QtWidgets.QLabel(self.centralwidget)
        self.node0_con.setGeometry(QtCore.QRect(230, 210, 131, 20))
        self.node0_con.setObjectName("node0_con")
        self.node_info[0]['con'] = self.node0_con
        self.node0_mode = QtWidgets.QLabel(self.centralwidget)
        self.node0_mode.setGeometry(QtCore.QRect(230, 190, 131, 20))
        self.node0_mode.setObjectName("node0_mode")
        self.node_info[0]['mode'] = self.node0_mode
        self.node0_name = QtWidgets.QLabel(self.centralwidget)
        self.node0_name.setGeometry(QtCore.QRect(230, 150, 131, 20))
        self.node0_name.setObjectName("node0_name")
        self.node_info[0]['name'] = self.node0_name

        self.node1_ip = QtWidgets.QLabel(self.centralwidget)
        self.node1_ip.setGeometry(QtCore.QRect(410, 170, 131, 20))
        self.node1_ip.setObjectName("node1_ip")
        self.node_info[1]['ip'] = self.node1_ip
        self.node1_con = QtWidgets.QLabel(self.centralwidget)
        self.node1_con.setGeometry(QtCore.QRect(410, 210, 131, 20))
        self.node1_con.setObjectName("node1_con")
        self.node_info[1]['con'] = self.node1_con
        self.node1_mode = QtWidgets.QLabel(self.centralwidget)
        self.node1_mode.setGeometry(QtCore.QRect(410, 190, 131, 20))
        self.node1_mode.setObjectName("node1_mode")
        self.node_info[1]['mode'] = self.node1_mode
        self.node1_name = QtWidgets.QLabel(self.centralwidget)
        self.node1_name.setGeometry(QtCore.QRect(410, 150, 131, 20))
        self.node1_name.setObjectName("node1_name")
        self.node_info[1]['name'] = self.node1_name

        self.node2_ip = QtWidgets.QLabel(self.centralwidget)
        self.node2_ip.setGeometry(QtCore.QRect(590, 170, 131, 20))
        self.node2_ip.setObjectName("node2_ip")
        self.node_info[2]['ip'] = self.node2_ip
        self.node2_con = QtWidgets.QLabel(self.centralwidget)
        self.node2_con.setGeometry(QtCore.QRect(590, 210, 131, 20))
        self.node2_con.setObjectName("node2_con")
        self.node_info[2]['con'] = self.node2_con
        self.node2_mode = QtWidgets.QLabel(self.centralwidget)
        self.node2_mode.setGeometry(QtCore.QRect(590, 190, 131, 20))
        self.node2_mode.setObjectName("node2_mode")
        self.node_info[2]['mode'] = self.node2_mode
        self.node2_name = QtWidgets.QLabel(self.centralwidget)
        self.node2_name.setGeometry(QtCore.QRect(590, 150, 131, 20))
        self.node2_name.setObjectName("node2_name")
        self.node_info[2]['name'] = self.node2_name

        self.node3_ip = QtWidgets.QLabel(self.centralwidget)
        self.node3_ip.setGeometry(QtCore.QRect(770, 170, 131, 20))
        self.node3_ip.setObjectName("node3_ip")
        self.node_info[3]['ip'] = self.node3_ip
        self.node3_con = QtWidgets.QLabel(self.centralwidget)
        self.node3_con.setGeometry(QtCore.QRect(770, 210, 131, 20))
        self.node3_con.setObjectName("node3_con")
        self.node_info[3]['con'] = self.node3_con
        self.node3_mode = QtWidgets.QLabel(self.centralwidget)
        self.node3_mode.setGeometry(QtCore.QRect(770, 190, 131, 20))
        self.node3_mode.setObjectName("node3_mode")
        self.node_info[3]['mode'] = self.node3_mode
        self.node3_name = QtWidgets.QLabel(self.centralwidget)
        self.node3_name.setGeometry(QtCore.QRect(770, 150, 131, 20))
        self.node3_name.setObjectName("node3_name")
        self.node_info[3]['name'] = self.node3_name

        self.node4_ip = QtWidgets.QLabel(self.centralwidget)
        self.node4_ip.setGeometry(QtCore.QRect(950, 170, 131, 20))
        self.node4_ip.setObjectName("node4_ip")
        self.node_info[4]['ip'] = self.node4_ip
        self.node4_con = QtWidgets.QLabel(self.centralwidget)
        self.node4_con.setGeometry(QtCore.QRect(950, 210, 131, 20))
        self.node4_con.setObjectName("node4_con")
        self.node_info[4]['con'] = self.node4_con
        self.node4_mode = QtWidgets.QLabel(self.centralwidget)
        self.node4_mode.setGeometry(QtCore.QRect(950, 190, 131, 20))
        self.node4_mode.setObjectName("node4_mode")
        self.node_info[4]['mode'] = self.node4_mode
        self.node4_name = QtWidgets.QLabel(self.centralwidget)
        self.node4_name.setGeometry(QtCore.QRect(950, 150, 131, 20))
        self.node4_name.setObjectName("node4_name")
        self.node_info[4]['name'] = self.node4_name
        
        self.node5_ip = QtWidgets.QLabel(self.centralwidget)
        self.node5_ip.setGeometry(QtCore.QRect(1130, 170, 131, 20))
        self.node5_ip.setObjectName("node5_ip")
        self.node_info[5]['ip'] = self.node5_ip
        self.node5_con = QtWidgets.QLabel(self.centralwidget)
        self.node5_con.setGeometry(QtCore.QRect(1130, 210, 131, 20))
        self.node5_con.setObjectName("node5_con")
        self.node_info[5]['con'] = self.node5_con
        self.node5_mode = QtWidgets.QLabel(self.centralwidget)
        self.node5_mode.setGeometry(QtCore.QRect(1130, 190, 131, 20))
        self.node5_mode.setObjectName("node5_mode")
        self.node_info[5]['mode'] = self.node5_mode
        self.node5_name = QtWidgets.QLabel(self.centralwidget)
        self.node5_name.setGeometry(QtCore.QRect(1130, 150, 131, 20))
        self.node5_name.setObjectName("node5_name")
        self.node_info[5]['name'] = self.node5_name

    def setUpButton(self):
        self.rx_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.rx_confirm.setGeometry(QtCore.QRect(245, 260, 121, 32))
        self.rx_confirm.setObjectName("rx_confirm")
        self.reset_mode = QtWidgets.QPushButton(self.centralwidget)
        self.reset_mode.setGeometry(QtCore.QRect(70, 290, 301, 41))
        self.reset_mode.setObjectName("reset_mode")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(270, 405, 100, 80))
        self.start_btn.setObjectName("start_btn")
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setGeometry(QtCore.QRect(270, 490, 100, 40))
        self.stop_btn.setObjectName("stop_btn")

    def setUpInput(self):
        self.rx_choose = QtWidgets.QComboBox(self.centralwidget)
        self.rx_choose.setGeometry(QtCore.QRect(125, 260, 120, 31))
        self.rx_choose.setObjectName("rx_choose")
        self.channel_choose = QtWidgets.QComboBox(self.centralwidget)
        self.channel_choose.setGeometry(QtCore.QRect(190, 345, 180, 21))
        self.channel_choose.setObjectName("channel_choose")
        self.collector_name = QtWidgets.QLineEdit(self.centralwidget)
        self.collector_name.setGeometry(QtCore.QRect(190, 375, 177, 21))
        self.collector_name.setObjectName("collector_name")
        self.collector_name.setPlaceholderText('Enter your name')
        self.collect_times = QtWidgets.QLineEdit(self.centralwidget)
        self.collect_times.setGeometry(QtCore.QRect(180, 420, 41, 21))
        self.collect_times.setObjectName("collect_times")
        self.collect_times.setText('3')
        self.collect_period = QtWidgets.QLineEdit(self.centralwidget)
        self.collect_period.setGeometry(QtCore.QRect(180, 460, 41, 21))
        self.collect_period.setObjectName("collect_period")
        self.collect_period.setText('60')
        self.break_period = QtWidgets.QLineEdit(self.centralwidget)
        self.break_period.setGeometry(QtCore.QRect(180, 500, 41, 21))
        self.break_period.setObjectName("break_period")
        self.break_period.setText('10')
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.setUpIcon()
        self.setUpNodeInfo()
        self.setUpButton()
        self.setUpInput()
        self.setRx = QtWidgets.QLabel(self.centralwidget)
        self.setRx.setGeometry(QtCore.QRect(80, 260, 60, 31))
        self.setRx.setObjectName("setRx")
        self.webcam = QtWidgets.QLabel(self.centralwidget)
        self.webcam.setGeometry(QtCore.QRect(400, 300, 320, 180))
        self.webcam.setObjectName("webcam")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(510, 260, 111, 31))
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.channelstring = QtWidgets.QLabel(self.centralwidget)
        self.channelstring.setGeometry(QtCore.QRect(80, 335, 111, 41))
        self.channelstring.setObjectName("channelstring")
        self.collectorname = QtWidgets.QLabel(self.centralwidget)
        self.collectorname.setGeometry(QtCore.QRect(80, 365, 111, 41))
        self.collectorname.setObjectName("collectorname")
        self.collecttimes = QtWidgets.QLabel(self.centralwidget)
        self.collecttimes.setGeometry(QtCore.QRect(80, 410, 111, 41))
        self.collecttimes.setObjectName("collecttimes")
        self.collectperiod = QtWidgets.QLabel(self.centralwidget)
        self.collectperiod.setGeometry(QtCore.QRect(80, 450, 201, 41))
        self.collectperiod.setObjectName("collectperiod")
        self.collectperiod.stackUnder(self.collect_times)
        self.breakperiod = QtWidgets.QLabel(self.centralwidget)
        self.breakperiod.setGeometry(QtCore.QRect(80, 490, 201, 41))
        self.breakperiod.setObjectName("breakperiod")
        self.breakperiod.stackUnder(self.break_period)
        self.instruct_bar = QtWidgets.QLabel(self.centralwidget)
        self.instruct_bar.setGeometry(QtCore.QRect(0, 550, 800, 40))
        self.instruct_bar.setObjectName("instruct_bar")
        self.instruct_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.instruct_bar.setFont(QtGui.QFont('Arial', 25))
        #set border color
        self.instruct_bar.setStyleSheet("border: 2px solid white;")
        # self.instruct_bar.setStyleSheet("background-color:transparent;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.local_nodename.setText(_translate("MainWindow", "name:"))
        self.local_ip.setText(_translate("MainWindow", "ip:"))
        self.local_mode.setText(_translate("MainWindow", "mode:"))
        self.local_con.setText(_translate("MainWindow", "connection:"))
        self.node0_ip.setText(_translate("MainWindow", "ip:"))
        self.node0_con.setText(_translate("MainWindow", "connection:"))
        self.node0_mode.setText(_translate("MainWindow", "mode:"))
        self.node0_name.setText(_translate("MainWindow", "name:"))
        self.node1_ip.setText(_translate("MainWindow", "ip:"))
        self.node1_con.setText(_translate("MainWindow", "connection:"))
        self.node1_mode.setText(_translate("MainWindow", "mode:"))
        self.node1_name.setText(_translate("MainWindow", "name:"))
        self.node2_ip.setText(_translate("MainWindow", "ip:"))
        self.node2_con.setText(_translate("MainWindow", "connection:"))
        self.node2_mode.setText(_translate("MainWindow", "mode:"))
        self.node2_name.setText(_translate("MainWindow", "name:"))
        self.node3_ip.setText(_translate("MainWindow", "ip:"))
        self.node3_con.setText(_translate("MainWindow", "connection:"))
        self.node3_mode.setText(_translate("MainWindow", "mode:"))
        self.node3_name.setText(_translate("MainWindow", "name:"))
        self.node4_ip.setText(_translate("MainWindow", "ip:"))
        self.node4_con.setText(_translate("MainWindow", "connection:"))
        self.node4_mode.setText(_translate("MainWindow", "mode:"))
        self.node4_name.setText(_translate("MainWindow", "name:"))
        self.node5_ip.setText(_translate("MainWindow", "ip:"))
        self.node5_con.setText(_translate("MainWindow", "connection:"))
        self.node5_mode.setText(_translate("MainWindow", "mode:"))
        self.node5_name.setText(_translate("MainWindow", "name:"))
        self.rx_confirm.setText(_translate("MainWindow", "confirm"))
        self.setRx.setText(_translate("MainWindow", "Set Rx:"))
        self.reset_mode.setText(_translate("MainWindow", "Reset mode"))
        self.label_18.setText(_translate("MainWindow", "Webcam viewer"))
        self.channelstring.setText(_translate("MainWindow", "Channel string:"))
        self.collectorname.setText(_translate("MainWindow", "Collector name:"))
        self.collecttimes.setText(_translate("MainWindow", "Collect times:"))
        self.collectperiod.setText(_translate("MainWindow", "Collect period:                  sec"))
        self.breakperiod.setText(_translate("MainWindow", "Break period:                    sec"))
        self.start_btn.setText(_translate("MainWindow", "Start!"))
        self.stop_btn.setText(_translate("MainWindow", "Stop!"))
        self.instruct_bar.setText(_translate("MainWindow", "IDLE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
