from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QColor, qRgb
from gui_window import Ui_MainWindow
from control_server import Server_Node
from threading import Thread, Event
import time
from Exec_Cmd import Exec_Cmd
import cv2
import yaml

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
		# in python3, super(Class, self).xxx = super().xxx
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.exec_cmd = Exec_Cmd()
        self.ui.setupUi(self)
        self.timer = QtCore.QTimer()
        self.server = Server_Node()
        self.cap = self.set_webcam()
        self.server.start()
        self.node_status = {"local":{"name":'', 'ip':'', 'conn':'', 'mode':'TX'}, 
                            "node0":{"name":'', 'ip':'', 'conn':'', 'mode':'TX'}, 
                            "node1":{"name":'', 'ip':'', 'conn':'', 'mode':'TX'}, 
                            "node2":{"name":'', 'ip':'', 'conn':'', 'mode':'TX'},
                            "node3":{"name":'', 'ip':'', 'conn':'', 'mode':'TX'},
                            "node4":{"name":'', 'ip':'', 'conn':'', 'mode':'TX'},
                            "node5":{"name":'', 'ip':'', 'conn':'', 'mode':'TX'},}
        self.stop_event = Event()
        self.save_video = None
        self.client_status_thread = Thread(target=self.get_node_status)
        self.client_status_thread.start()
        self.set_icon()
        self.activate_btn()
        self.timer.timeout.connect(self.webcam_loader)
        self.timer.start(1)
        with open('./channel_list.yaml') as f:
            channel_list = yaml.load(f, yaml.CFullLoader)
            self.ui.channel_choose.addItems(channel_list)
        print("[SERVER INFO] Server is running.")

    def set_webcam(self):
        cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
        cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        cap.set(cv2.CAP_PROP_FPS, 30)

        return cap
    
    def get_node_status(self):
        while not self.stop_event.is_set():
            self.node_status['local']['name'] = self.exec_cmd.run("whoami")[0][0]
            self.node_status['local']['ip'] = self.server.local_ip
            self.node_status['local']['conn'] = 'connected'
            reflash = False
            for id, node in enumerate(list(self.node_status.keys())[1:]):
                if len(self.server.client_status) > id:
                    addr = list(self.server.client_status.keys())[id]
                    if self.node_status[node]['ip'] != addr[0] or self.node_status[node]['name'] != self.server.client_status[addr]['username']:
                        reflash = True
                    self.node_status[node]['ip'] = addr[0]
                    self.node_status[node]['name'] = self.server.client_status[addr]['username']
                    self.node_status[node]['conn'] = self.server.client_status[addr]['status']
                else:
                    if self.node_status[node]['conn'] != 'lost':
                        reflash = True
                    self.node_status[node]['ip'] = 'None'
                    self.node_status[node]['name'] = 'None'
                    self.node_status[node]['conn'] = 'lost'
                    self.node_status[node]['mode'] = 'TX'
            if reflash:
                self.show_client_status()
            time.sleep(1)

    def show_client_status(self):
        self.ui.rx_choose.clear()
        self.ui.rx_choose.addItem(f'0:local')
        self.ui.local_mode.setText(f'mode: {self.node_status["local"]["mode"]}')
        for id in range(len(self.ui.node_info)):
            node = list(self.node_status.keys())[id+1]
            if self.node_status[node]['conn'] == 'connected':
                print(f'node{node} connected, set to green.')
                self.ui.node_icon[id].setBackgroundBrush(QColor(qRgb(200, 255, 200)))
                self.ui.rx_choose.addItem(f'{id+1}:{self.node_status[node]["name"]}')
            else:
            	print(f'node disconnected, set to red.')
            	self.ui.node_icon[id].setBackgroundBrush(QColor(qRgb(255, 200, 200)))
            self.ui.node_info[id]['ip'].setText(f'ip: {self.node_status[node]["ip"]}')
            self.ui.node_info[id]['con'].setText(f'conn: {self.node_status[node]["conn"]}')
            self.ui.node_info[id]['name'].setText(f'name: {self.node_status[node]["name"]}')
            self.ui.node_info[id]['mode'].setText(f'mode: {self.node_status[node]["mode"]}')
            

    def set_icon(self):
        server_icon = QtGui.QPixmap('./server_icon.png').scaled(121, 121)
        client_icon = QtGui.QPixmap('./client_icon.png').scaled(121, 121)
        self.ui.local_scene.addPixmap(server_icon)
        self.ui.node0_scene.addPixmap(client_icon)
        self.ui.node1_scene.addPixmap(client_icon)
        self.ui.node2_scene.addPixmap(client_icon)
        self.ui.node3_scene.addPixmap(client_icon)
        self.ui.node4_scene.addPixmap(client_icon)
        self.ui.node5_scene.addPixmap(client_icon)
        self.ui.local_con.setText('conn: connected')
        self.ui.local_mode.setText('mode: TX')
        self.ui.local_nodename.setText(f'name: {self.exec_cmd.run("whoami")[0][0]}')
        self.ui.local_ip.setText(f'ip: {self.server.local_ip}')
    
    def webcam_loader(self):
        ret, frame = self.cap.read()
        if frame is not None:
            if self.save_video is not None:
                cv2.imwrite(f'{self.save_video}/{time.time_ns()}.jpg', frame)
            else:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1]*3, QtGui.QImage.Format_RGB888)
                img = QtGui.QPixmap.fromImage(img).scaled(320, 180)
                self.ui.webcam.setPixmap(img)
        else:
            print('WebcamLoader: failed to get frame')
            self.stop_event.set()

    def onclick_rx_confirm(self):
        rx_id = self.ui.rx_choose.currentIndex()
        if rx_id == 0:
            self.ui.local_mode.setText('mode: RX')
            self.node_status['local']['mode'] = 'RX'
        else:
            addr = list(self.server.client_status.keys())[rx_id-1]
            node = list(self.node_status.keys())[rx_id]
            self.ui.node_info[rx_id-1]['mode'].setText(f'mode: RX')
            self.node_status[node]['mode'] = 'RX'
            self.server.sendTextViaSocket('set,RX', addr)

    def onclick_reset_mode(self):
        self.exec_cmd.run('echo reset')
        for addr in self.server.client_status:
            self.server.sendTextViaSocket('set,TX', addr)
        for node in self.node_status:
            self.node_status[node]['mode'] = 'TX'
        self.show_client_status()

    def onclick_start(self):
        self.curr_stat = 'idle'
        self.stop = Event()
        def start_collect():
            collect_period = int(self.ui.collect_period.text())
            collect_times = int(self.ui.collect_times.text())
            break_period = int(self.ui.break_period.text())
            collector_name = self.ui.collector_name.text()
            # ----------------------------stdby session---------------------------- #
            self.curr_stat = 'stdby'
            channel = self.ui.channel_choose.currentText().split(' ')[1]
            filename = self.exec_cmd.exec(f'stdby {collector_name} {channel}')
            for addr in self.server.client_status:
                self.server.sendTextViaSocket(f'exec,stdby {collector_name} {channel}', addr)
            time.sleep(10)
            # ----------------------------stdby session---------------------------- #
            for i in range(collect_times):
                if self.stop.is_set():
                    break
                # ----------------------------collecting session---------------------------- #
                self.exec_cmd.exec('beep 1')
                print("[SERVER INFO] Start collecting data.")
                self.curr_stat = 'collecting' 
                self.save_video = f'./{collector_name}/{filename}'
                self.exec_cmd.exec(f'start {self.node_status["local"]["mode"]} ./{collector_name}/{filename}')
                for addr in self.server.client_status:
                    self.server.sendTextViaSocket(f'exec,start -- ./{collector_name}/{filename}', addr)
                self.stop.wait(collect_period)
                # ----------------------------collecting session---------------------------- #
                # ----------------------------break session---------------------------- #
                self.exec_cmd.exec('beep 2')
                print("[SERVER INFO] Stop collecting data.")
                self.curr_stat = 'stop'
                self.save_video = None
                if i == collect_times-1:
                    collector_name = '--'
                    self.stop.set()
                filename = self.exec_cmd.exec(f'stop')
                for addr in self.server.client_status:
                    self.server.sendTextViaSocket(f'exec,stop', addr)
                self.stop.wait(break_period)
                # ----------------------------break session---------------------------- #
            self.curr_stat = 'idle'
            self.stop.set()

        def change_color():
            while not self.stop.is_set():
                if self.curr_stat == 'stdby':
                    self.ui.instruct_bar.setText("Standby")
                    self.ui.instruct_bar.setStyleSheet("background-color: #A3FF72;"
                                                       "color: black;")
                elif self.curr_stat == 'collecting':
                    self.ui.instruct_bar.setText("Collecting")
                    self.ui.instruct_bar.setStyleSheet("background-color: #FF5454;"
                                                       "color: black;")
                elif self.curr_stat == 'stop':
                    self.ui.instruct_bar.setText("Break")
                    self.ui.instruct_bar.setStyleSheet("background-color: #FFFF4A;"
                                                       "color: black;")
                time.sleep(0.5)
            self.ui.instruct_bar.setText("IDLE")
            self.ui.instruct_bar.setStyleSheet("background-color:transparent;"
                                               "color: white;"
                                               "border: 2px solid white;")
        collect_thread = Thread(target=start_collect)
        collect_thread.start()
        color_thread = Thread(target=change_color)
        color_thread.start()
    
    def onclick_stop(self):
        self.stop.set()
        self.stop_event.set()
        self.curr_stat = 'idle'
        self.save_video = None
        self.exec_cmd.exec('stop')
        for addr in self.server.client_status:
            self.server.sendTextViaSocket(f'exec,stop --', addr)

    def activate_btn(self):
        self.ui.start_btn.clicked.connect(self.onclick_start)
        self.ui.rx_confirm.clicked.connect(self.onclick_rx_confirm)
        self.ui.reset_mode.clicked.connect(self.onclick_reset_mode)
        self.ui.stop_btn.clicked.connect(self.onclick_stop)
    

        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
