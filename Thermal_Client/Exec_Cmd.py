import subprocess
import os
import time
import signal
import threading

# array_prepare_for_picoscenes 3 "5640 160 5250"
class Exec_Cmd():
    def __init__(self) -> None:
        self.process = subprocess.Popen('echo "Ready to execute command!"', shell=True)

    def run(self, cmd: str):
        self.process = subprocess.Popen(cmd, shell=False)
        # stdout, stderr = self.process.communicate()
        # stdout = stdout.strip().decode('utf-8').split('\n')
        # stderr = stderr.strip().decode('utf-8').split('\n')
        # return stdout, stderr

    def exec(self, cmd: str):
        cmd = cmd.split(' ')
        if cmd[0] == 'stdby':
            print("Thermal Pi standby")
            timestring = time.strftime("%y%m%d_%H%M%S", time.localtime())
            return timestring

        elif cmd[0] == 'start':
            folder_path = f"{cmd[2]}"
            os.makedirs(folder_path, exist_ok=True)
            cmd = f"python3 /home/pi/FLIR/dual_preview.py --save --folder_path {folder_path}"
            self.run(cmd.split())
            # print(stdout)
            # print(stderr)

        elif cmd[0] == 'stop':
            self.process.terminate()
            timestring = time.strftime("%y%m%d_%H%M%S", time.localtime())
            return timestring

        elif cmd[0] == 'beep' and cmd[1] == '1':
            self.run('beep -f 2000 -r 1 -d 100 -l 50')

        elif cmd[0] == 'beep' and cmd[1] == '2':
            self.run('beep -f 2000 -r 2 -d 100 -l 50')