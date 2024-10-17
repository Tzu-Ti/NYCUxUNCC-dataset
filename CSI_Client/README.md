# Wi-Fi CSI Data Collection

Collect specified Wi-Fi CSI packets using the Wi-Fi 6 protocol through the package PicoScenes.

## Setting Ethernet
Set statics ip to be in a local network with server.
- Client1: 192.168.5.3
- Client2: 192.168.5.4
- Client3: 192.168.5.5

## Prerequisite
### Download related package from [here](https://ps.zpj.io/)

## Start socket client
### Set servier ip and port at `line 12` in `control_client.py`
```python=12
self.server_ip = '192.168.5.2'
self.server_port = 51000
```
### Set NIC ID, bandwidth and channel
> array_prepare_for_picoscenes `NIC ID` "`primary channel` `bandwidth` `center channel`"
```shell!
$ array_prepare_for_picoscenes 3 "6275 160 6345"
```
### Execute the client code
```shell!
$ python3 control_client.py
```