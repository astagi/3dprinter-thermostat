# -*- coding: utf-8 -*-
from ds18b20 import DS18B20

def get_temperature():
    sensor = DS18B20()
    return sensor.get_temperature()

def get_threshold():
    # for now we hardcode the threshold
    return 25.0

def heat_on():
    pass

def heat_off():
    pass

def check():
    if get_temperature() > get_threshold():
        heat_on()
    else:
        heat_off()

if __name__ == '__main__':
    while True:
        check()