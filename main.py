#!/usr/bin/python

import os

COMMAND     = os.getenv('COMMAND')
DEVICE_NAME = os.getenv('DEVICE_NAME', 'Shutter3')

from evdev import InputDevice, ecodes
import evdev, time

def callback(event):
    if event.type == ecodes.EV_KEY and event.value == 1:
        os.system(COMMAND)

def read_event(device_path, callback):
    while (True):
        try:
            for event in InputDevice(device_path).read_loop():
                callback(event)
        except OSError as e:
            if e.errno != 6 and e.errno != 19:
                raise
        time.sleep(1)

def get_device_path(device_name):
    while (True):
        try:
            for device in [InputDevice(path) for path in evdev.list_devices()]:
                if (device_name in device.name):
                    return device.path
        except OSError as e:
            if e.errno != 6:
                raise
        time.sleep(1)

def main():
    device_path = get_device_path(DEVICE_NAME)
    read_event(device_path, callback)

if __name__ == '__main__':
    main()
