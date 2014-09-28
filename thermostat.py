# -*- coding: utf-8 -*-
from ds18b20 import DS18B20
from RPi import GPIO
import os

def get_temperature():
    sensor = DS18B20()
    return sensor.get_temperature()

def get_threshold():
    # for now we hardcode the threshold
    return 25.0

def heat_on():
    GPIO.output(17,GPIO.LOW)

def heat_off():
    GPIO.output(17,GPIO.HIGH)

def check():
    if get_temperature() < get_threshold():
        heat_on()
    else:
        heat_off()

if __name__ == '__main__':
    os.system('sudo modprobe w1-gpio')
    os.system('sudo modprobe w1-therm')
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    while True:
        check()