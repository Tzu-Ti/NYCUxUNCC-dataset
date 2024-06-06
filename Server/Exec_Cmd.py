import subprocess
import os
import time
import signal

# array_prepare_for_picoscenes 3 "5640 160 5250"
class Exec_Cmd():
    def __init__(self) -> None:
        self.process = subprocess.Popen('echo "Ready to execute command!"', shell=True)

    def run(self, cmd: str):
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        stdout = stdout.strip().decode('utf-8').split('\n')
        stderr = stderr.strip().decode('utf-8').split('\n')
        return stdout, stderr
    
    def exec(self, cmd: str):
        cmd = cmd.split(' ')
        if cmd[0] == 'stdby':
            #self.run(f'array_prepare_for_picoscenes 6 {cmd[2].replace("_", " ")}')
            print(f'echo \'array_prepare_for_picoscenes 6 {cmd[2].replace("_", " ")}\'')
            if not os.path.exists(f'./{cmd[1]}'):
                self.run(f'mkdir {cmd[1]}')
            timestring = time.strftime("%y%m%d_%H%M%S", time.localtime())
            return timestring
        
        elif cmd[0] == 'start':
            self.run(f'mkdir -p {cmd[2]}')
            if cmd[1] == 'RX':
                #run_cmd = 'PicoScenes "-i 6 --mode logger"'.split(" ")
                self.process = subprocess.Popen(f'cd {cmd[2]} && PicoScenes "-i 6 --mode logger"', shell=True, preexec_fn=os.setsid)
            elif cmd[1] == 'TX':
                #run_cmd = 'PicoScenes "-i 6 --mode injector --preset TX_CBW_160_HESU --repeat 1e5 --delay 5e3"'.split(" ")
                self.process = subprocess.Popen(f'cd {cmd[2]} && PicoScenes "-i 6 --mode injector --preset TX_CBW_160_HESU --repeat 1e5 --delay 2e3"', shell=True, preexec_fn=os.setsid)

        elif cmd[0] == 'stop':
            print('stop')
            os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
            timestring = time.strftime("%y%m%d_%H%M%S", time.localtime())
            return timestring

        elif cmd[0] == 'beep' and cmd[1] == '1':
            self.run('beep -f 2000 -r 1 -d 100 -l 50')
        
        elif cmd[0] == 'beep' and cmd[1] == '2':
            self.run('beep -f 2000 -r 2 -d 100 -l 50')
