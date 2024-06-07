# Depth Data Collection

Collect in-depth information using an orbbec femto bolt.

## Prerequisite
### Download related package from [pyorbbecsdk](https://github.com/orbbec/pyorbbecsdk)
```shell!
$ git clone https://github.com/orbbec/pyorbbecsdk.git
$ sudo apt-get install python3-dev python3-venv python3-pip python3-opencv
```

### Custom Python3 Path (Optional)
If you use Anaconda, set the Python3 path to the Anaconda path in pyorbbecsdk/CMakeLists.txt before the find_package(Python3 REQUIRED COMPONENTS Interpreter Development) line:
```shell!
$ set(Python3_ROOT_DIR "/home/anaconda3/envs/py3.6.8") # Replace with your Python3 path
$ set(pybind11_DIR "${Python3_ROOT_DIR}/lib/python3.6/site-packages/pybind11/share/cmake/pybind11") # Replace with your Pybind11 path
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

### Try the Examples
```shell!
$ cd pyorbbecsdk
$ export PYTHONPATH=$PYTHONPATH:$(pwd)/install/lib/
$ sudo bash ./scripts/install_udev_rules.sh
$ sudo udevadm control --reload-rules && sudo udevadm trigger
$ python3 examples/depth_color_sync_align_viewer.py
```

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
