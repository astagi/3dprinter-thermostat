# -*- coding: utf-8 -*-

def get_temperature(pin):
    pass

def get_threshold():
    # for now we hardcode the threshold
    pass

def heat_on():
    pass

def heat_off():
    pass

def check(pin):
    if get_temperature(pin) > get_threshold():
        heat_on()
    else:
        heat_off()

if __name__ == '__main__':
    while True:
        check(12)