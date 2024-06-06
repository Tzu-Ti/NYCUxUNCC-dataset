# Thermal Data Collection

Use lepton thermal to collect data on Raspberry Pi, and execute socket client to achieve multi-machine connection to collect data.

## Prerequisite
### Download related package
```shell!
$ sudo apt-get update
$ sudo apt-get install python3-opencv -y
```
### Download pylepton
```shell!
$ git clone https://github.com/groupgets/pylepton.git -b lepton3-dev
$ cd pylepton
$ sudo python3 setup.py install
```
## Test pylepton and dual camera
```shell!
$ python3 dual_preview.py --preview
```

## Start socket client
### Set servier ip and port in `control_client.py`
```python=12
self.server_ip = '192.168.5.2'
self.server_port = 51000
```
