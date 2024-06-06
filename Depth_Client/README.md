# Depth Data Collection

Collect in-depth information using an orbbec femto bolt.

## Prerequisite
### Download related package from [pyorbbecsdk](https://github.com/orbbec/pyorbbecsdk)
```shell!
$ git clone https://github.com/orbbec/pyorbbecsdk.git
$ sudo apt-get install python3-dev python3-venv python3-pip python3-opencv
```
### Build the SDK
```shell!
$ cd pyorbbecsdk
$ python3 -m venv ./venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
$ mkdir build
$ cd build
$ cmake -Dpybind11_DIR=`pybind11-config --cmakedir` ..
$ make -j4
$ make install
```
### Move the built package to virtual environment package folder

## Start socket client
### Set servier ip and port at `line 8` in `control_client.py`
```python=12
self.server_ip = '192.168.5.2'
self.server_port = 51000
```
### Execute the client code
```shell!
$ python3 control_client.py
```