# Data Collection Server

Execute the data collection server and create a GUI to set data collection parameters.
Establish a data collection process, including collection times, collection time, rest time, and record through webcam at the same time.

![GUI](gui.jpg)

## Execute collection server
```shell!
$ python3 gui_function.py
```

1. set csi collection client to Rx
2. set channel string, we choose `65 "6275_160_6345"`
3. set collector name
4. set collect times
5. set collect period
6. set break period

## Start collect
press the `Start!` button, then the server will send a message to all client to start collecting.

After the collecting time which you have already set, server will send a message again to stop the collecting.