# Thermal Data Collection

Use lepton thermal to collect data on Raspberry Pi, and execute socket client to achieve multi-machine connection to collect data.

## Prerequisite
### Download related package from [here](https://ps.zpj.io/)

## Start socket client
### Set servier ip and port at `line 12` in `control_client.py`
```python=12
self.server_ip = '192.168.5.2'
self.server_port = 51000
```
### Execute the client code
```shell!
$ python3 control_client.py
```